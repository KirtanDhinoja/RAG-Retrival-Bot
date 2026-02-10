import os
from typing import TypedDict, List
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

# Define the data structure for our Graph
class GraphState(TypedDict):
    question: str
    context: List[str]
    answer: str

# 1. Initialize Embeddings (Must match ingest.py exactly)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    task_type="retrieval_query" # Note: 'retrieval_query' is best for the chat side
)

# 2. Connect to Pinecone
vectorstore = PineconeVectorStore(
    index_name="agentic-ai-index", 
    embedding=embeddings
)

# 3. Initialize the LLM (Gemini 1.5 Flash is free and fast)
llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", temperature=0)

# --- Graph Nodes ---

def retrieve(state: GraphState):
    """Fetch relevant chunks from Pinecone"""
    print(f"--- RETRIEVING CONTEXT FOR: {state['question']} ---")
    docs = vectorstore.similarity_search(state["question"], k=4)
    content = [d.page_content for d in docs]
    return {"context": content}

def generate(state: GraphState):
    """Generate answer strictly grounded in context"""
    print("--- GENERATING ANSWER ---")
    
    prompt = f"""You are an expert AI Assistant. Use ONLY the provided context to answer the question. 
    If the answer is not in the context, say: 'I'm sorry, the provided eBook does not contain information on this topic.'
    
    Context:
    {state['context']}
    
    Question: 
    {state['question']}
    
    Final Answer:"""
    
    response = llm.invoke(prompt)
    return {"answer": response.content}

# --- Construct LangGraph ---

workflow = StateGraph(GraphState)
workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)

workflow.set_entry_point("retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

# Compile the app
rag_app = workflow.compile()