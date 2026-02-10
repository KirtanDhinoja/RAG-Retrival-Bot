# 🤖 Agentic AI RAG Chatbot

A **stateful, agent-driven Retrieval-Augmented Generation (RAG) chatbot** built using **LangGraph** and **Google Gemini Flash**, strictly grounded in the *Agentic AI* eBook.  
Unlike traditional linear RAG pipelines, this system models the workflow as a **state machine**, enabling fine-grained control over retrieval, context flow, and generation.

---

## 📌 Overview

This project implements an **Agentic RAG architecture** where retrieval and generation are orchestrated using **LangGraph**. The chatbot answers user queries **only from the ingested knowledge base**, effectively minimizing hallucinations and ensuring factual consistency.

Key highlights:
- Stateful agent workflow (not a simple chain)
- Strict context grounding using retrieved documents
- Optimized to run reliably on **Google AI Studio free-tier limits**

---

## 🧠 Architecture

The system is designed as a **stateful RAG pipeline** with explicit control over each stage.

### 1. Ingestion Pipeline
- Source: *Agentic AI* eBook (PDF)
- Loader: `PyPDFLoader`
- Chunking: `RecursiveCharacterTextSplitter`
- Strategy: Semantic chunking to preserve contextual coherence within LLM context windows

### 2. Vector Memory
- Embedding Model: `gemini-embedding-001`
- Vector Dimension: **3072**
- Vector Store: **Pinecone (Serverless)**
- Purpose: High-speed semantic similarity search over document chunks

### 3. Agentic State Machine (LangGraph)
Instead of a linear chain, the workflow is modeled as a **state machine**:

- **Retrieve Node**
  - Performs top-K similarity search in Pinecone
  - Fetches the most relevant document chunks

- **Generate Node**
  - Uses **Gemini 2.5 / 3 Flash**
  - A strict system prompt ensures responses are generated **only from retrieved context**
  - Prevents hallucinations and out-of-scope answers

LangGraph manages transitions between these nodes, enabling controlled and debuggable agent behavior.

---

## 🛡️ Hallucination Control

To ensure reliability:
- The LLM is constrained by a **strict system prompt**
- Responses are generated **only from retrieved Pinecone context**
- No external or prior model knowledge is allowed during generation

This makes the chatbot suitable for **knowledge-critical use cases**.

---

## 🚦 Rate Limiting & Stability

Google AI Studio free tier enforces a **100 RPM limit**.  
To handle this reliably:
- Manual request batching is implemented
- Controlled time delays are introduced between LLM calls
- Ensures stable performance without quota errors

---

## 🧩 Tech Stack

- **LLM**: Google Gemini 2.5 / Gemini 3 Flash (Free Tier)
- **Embeddings**: `gemini-embedding-001`
- **Vector Database**: Pinecone (Serverless)
- **Orchestration**: LangChain + LangGraph
- **Backend**: Python
- **UI**: Streamlit

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- Pinecone account
- Google AI Studio API key

### Installation
```bash
git clone https://github.com/your-username/agentic-ai-rag-chatbot.git
cd agentic-ai-rag-chatbot
pip install -r requirements.txt
