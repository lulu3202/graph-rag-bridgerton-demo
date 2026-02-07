# Graph RAG vs Traditional RAG Demo

Minimal comparison of Traditional RAG and Graph RAG using the Bridgerton "Lady in Silver" mystery.

---

## Question

Who is the Lady in Silver and how is she connected to Lord Penwood?

---

## Purpose

Both systems use the same facts but different representations:

**Traditional RAG**  
Stores text chunks and retrieves via vector similarity.

**Graph RAG**  
Stores entities and relationships and retrieves via graph traversal.

---

## Tech Stack
- LLM: Llama 3.2 3B via Ollama
- Embeddings: sentence-transformers
- Vector Search: FAISS
- Graph: JSON
- Environment: uv

---

## Prerequisites

Install Ollama:

```bash
brew install ollama
```

Pull model:

```bash
ollama pull llama3.2:3b
```

Ensure Ollama is running:

```bash
ollama serve
```

---

## Setup

From the project root:

```bash
cd graph-rag-bridgerton-demo
```

Create and activate environment:

```bash
uv venv
source .venv/bin/activate
```

Install dependencies:

```bash
uv sync
```

---

## Run

From project root:

**Traditional RAG**
```bash
python traditional_rag/rag.py
```

**Graph RAG**
```bash
python graph_rag/graph_rag.py
```

---

## Key Insight

Traditional RAG retrieves similar text.  
Graph RAG retrieves structured relationships.

For this mystery, correct reasoning requires multi-hop connections:

```
Sophie Baek → Lady in Silver
Sophie Baek → Lord Penwood
```

Graph RAG makes these connections explicit.

---

## Data

`data/documents.txt` — Text corpus  
`data/graph.json` — Knowledge graph
