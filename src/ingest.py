import os
import time
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

def ingest():
    # 1. Load the eBook
    loader = PyPDFLoader("data/Ebook-Agentic-AI.pdf")
    docs = loader.load()
    
    # 2. Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    print(f"Total chunks created: {len(chunks)}")

    # 3. Initialize Embeddings (Native 3072 dimensions)
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        task_type="retrieval_document"
    )
    
    # 4. Initialize Vector Store
    vector_store = PineconeVectorStore(
        index_name="agentic-ai-index", 
        embedding=embeddings
    )

    # 5. Batch Ingestion with Rate Limiting
    batch_size = 50 
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        
        vector_store.add_documents(batch)
        print(f"✅ Successfully uploaded chunks {i} to {min(i + batch_size, len(chunks))}")
        
        if i + batch_size < len(chunks):
            print("⏳ Waiting 20 seconds for Free Tier quota...")
            time.sleep(20) # Slightly longer sleep to be safe

    print("\n🚀 SUCCESS! Your index is ready.")

if __name__ == "__main__":
    ingest()