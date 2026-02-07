# Graph RAG vs Traditional RAG Demo

A minimal comparison of Traditional RAG and Graph RAG using Harry Potter's Dumbledore death storyline.

## Purpose

Both approaches use the same facts but different structures:
- **Traditional RAG**: Stores text chunks, embeds them, retrieves similar chunks via vector search
- **Graph RAG**: Stores entities and relationships, retrieves connected nodes, reasons over structure

## Question

"Why did Dumbledore allow Snape to kill him?"

## Setup

1. Navigate to project:
```bash
cd graph-rag-harry-potter-demo
```

2. Add your OpenAI API key to `.env`:
```
OPENAI_API_KEY=sk-your-key-here
```

3. Load environment variables:
```bash
source .env  # On Windows: set -a; . .env; set +a
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

### Graph RAG

```bash
cd graph_rag
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
python graph_rag.py
```

## Comparison

Traditional RAG retrieves text chunks based on semantic similarity. Graph RAG retrieves structured relationships between entities. Both send context to an LLM, but Graph RAG provides explicit connections that can reveal multi-hop reasoning paths.
