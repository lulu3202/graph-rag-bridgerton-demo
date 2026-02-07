import ollama
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Embedding model
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# Load documents
with open("../data/documents.txt", "r") as f:
    text = f.read()

# Split by single newline (since each document is one line)
chunks = [line.strip() for line in text.split("\n") if line.strip()]

# 1. Create embeddings
embeddings = embed_model.encode(chunks)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings, dtype="float32"))

# 2. Query
query = "Who was the Lady in Silver and how is she connected to the Penwood family?"

q_emb = embed_model.encode([query])
q_emb = np.array(q_emb, dtype="float32")

# 3. Retrieve Top-3
_, indices = index.search(q_emb, 3)
retrieved_chunks = [chunks[i] for i in indices[0]]
retrieved = "\n\n".join(retrieved_chunks)

# 4. Generate with Ollama
final_res = ollama.chat(
    model='llama3.2:3b',
    options={"temperature": 0},
    messages=[
        {"role": "system", "content": "Answer strictly based on the provided context."},
        {"role": "user", "content": f"Context:\n{retrieved}\n\nQuestion: {query}"}
    ]
)

print("=== TRADITIONAL RAG ===")
print("\nRetrieved chunks:")
for chunk in retrieved_chunks:
    print("-", chunk)

print("\nAnswer:")
print(final_res["message"]["content"])