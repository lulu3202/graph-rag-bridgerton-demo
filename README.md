# Graph RAG vs Traditional RAG Demo

A minimal comparison of Traditional RAG and Graph RAG using Bridgerton's "Lady in Silver" mystery storyline.

## Purpose

Both approaches use the same facts but different structures:
- **Traditional RAG**: Stores text chunks, embeds them, retrieves similar chunks via vector search
- **Graph RAG**: Stores entities and relationships, retrieves connected nodes, reasons over structure

## Question

"Who is the Lady in Silver and how is she connected to Lord Penwood?"

## Tech Stack

- **LLM**: Llama 3.2 3B via Ollama (runs locally)
- **Embeddings**: sentence-transformers (all-MiniLM-L6-v2)
- **Vector Search**: FAISS
- **Graph Storage**: JSON

## Prerequisites

1. Install Ollama:
```bash
brew install ollama
```

2. Pull Llama 3.2 3B:
```bash
ollama pull llama3.2:3b
```

3. Ensure Ollama is running (usually auto-starts, or run `ollama serve`)

## Setup

Navigate to project:
```bash
cd graph-rag-harry-potter-demo
```

## Run

### Traditional RAG

```bash
cd traditional_rag
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
python rag.py
```

**How it works:**
1. Loads 6 text documents about the Bridgerton mystery
2. Embeds each document using sentence-transformers
3. Retrieves top 3 most similar documents via FAISS vector search
4. Sends retrieved chunks to Llama 3.2 for answer generation

### Graph RAG

```bash
cd ../graph_rag
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
python graph_rag.py
```

**How it works:**
1. Loads knowledge graph with 7 entities and 7 relationships
2. Extracts entities from the query (e.g., "Lady in Silver", "Lord Penwood")
3. Retrieves all edges connected to those entities (2-hop traversal)
4. Sends structured relationships to Llama 3.2 for reasoning

## Comparison

| Aspect | Traditional RAG | Graph RAG |
|--------|----------------|-----------|
| **Storage** | Text chunks | Entities + Relationships |
| **Retrieval** | Semantic similarity (vector search) | Graph traversal (entity matching) |
| **Context** | Top-K similar documents | Connected relationships |
| **Reasoning** | Implicit (in text) | Explicit (in graph structure) |
| **Multi-hop** | Limited by chunk boundaries | Natural via graph traversal |

**Key Insight**: Graph RAG excels at multi-hop reasoning. To answer "Who is the Lady in Silver?", you need to connect:
- Lady in Silver → Silver Glove → Lord Penwood → Sophie Baek

Traditional RAG may miss this connection if the facts are split across different chunks that don't rank highly in similarity.

## Data Files

- `data/documents.txt`: 6 text documents about the Bridgerton mystery
- `data/graph.json`: Knowledge graph with entities and relationships

## Why Local LLM?

- **Free**: No API costs
- **Private**: Data stays on your machine
- **Fast**: No network latency
- **Offline**: Works without internet (after model download)
