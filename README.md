# 🤖 Agentic AI RAG Chatbot

## 🚀 Project Overview
This project is a high-performance, RAG-based (Retrieval-Augmented Generation) AI Chatbot built strictly to assist executives in understanding **Agentic AI**. It utilizes **LangGraph** for stateful orchestration and **Pinecone** for high-dimensional vector storage.

The chatbot is grounded exclusively in the **"Agentic AI for Executives"** eBook, ensuring all responses are factual and cited from the provided knowledge base.

## 🧠 Architecture
- **Stateful Orchestration**: Built with **LangGraph** to manage a robust two-stage pipeline (Retrieve -> Generate).
- **Vector Memory**: Uses **Pinecone** to store 3072-dimensional embeddings of the eBook content.
- **LLM Integration**: Powered by **Google Gemini 3 Flash** for fast, cost-effective, and accurate reasoning.
- **Strict Grounding**: Implemented a validation layer to prevent hallucinations; if the answer isn't in the eBook, the bot will notify the user.

## 🛠️ Tech Stack (Zero-Cost Focus)
- **Orchestration**: LangChain, LangGraph
- **Vector Database**: Pinecone (Serverless)
- **Embeddings**: Google `gemini-embedding-001`
- **LLM**: Google `gemini-1.5-flash-latest`
- **UI**: Streamlit
- **Document Loading**: PyPDF

## 🧪 Sample Queries for Testing
Use these specific queries to verify the bot's grounding in the "Agentic AI for Executives" eBook:

1. **Grounded Retrieval**: "What are the five core pillars of Agentic AI defined in the book?"
2. **Conceptual Reasoning**: "Explain the difference between traditional AI, non-agentic AI, and agentic systems."
3. **Industry Application**: "How can Agentic AI be used to solve a crisis in a global supply chain?"
4. **Technical Specifics**: "What is the BDI model in agent-oriented programming according to the text?"
5. **Hallucination Prevention**: "What does the eBook say about the best way to train a pet dog?" (The bot should state it doesn't know).

## ⚙️ Setup & Installation
1. **Clone the Repo**: `git clone <your-repo-link>`
2. **Install Dependencies**: `pip install -r requirements.txt`
3. **Environment Variables**: Create a `.env` file with your `GOOGLE_API_KEY` and `PINECONE_API_KEY`.
4. **Ingest Data**: Run `python src/ingest.py` to populate your vector database.
5. **Launch App**: Run `streamlit run src/app.py`.