import json
import ollama

# 1. Load the Graph
with open("../data/graph.json", "r") as f:
    graph = json.load(f)

# 2. Query (Bridgerton universe)
query = "Who is the Lady in Silver and how is she connected to Lord Penwood?"

# 3. Entity Matching
# Match node names directly from the query
extracted_entities = [
    node["id"]
    for node in graph["nodes"]
    if node["id"].lower() in query.lower()
]

# 4. Retrieve Relevant Edges (One-hop)
relevant_edges = [
    e for e in graph["edges"]
    if e["source"] in extracted_entities or e["target"] in extracted_entities
]

# 5. Expand to Two-Hop (important for reasoning)
connected_entities = set()
for edge in relevant_edges:
    connected_entities.add(edge["source"])
    connected_entities.add(edge["target"])

expanded_edges = [
    e for e in graph["edges"]
    if e["source"] in connected_entities or e["target"] in connected_entities
]

# Remove duplicates
unique_edges = {
    f"{e['source']}-{e['relation']}-{e['target']}": e
    for e in expanded_edges
}.values()

# 6. Serialize relationships
context = "Social Connections & Secrets:\n"
for edge in unique_edges:
    context += f"- {edge['source']} {edge['relation']} {edge['target']}\n"

# 7. Generate Answer using Ollama
response = ollama.chat(
    model="llama3.2:3b",
    options={"temperature": 0},
    messages=[
        {
            "role": "system",
            "content": "Answer strictly based on the provided relationships."
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {query}"
        }
    ]
)

print("=== GRAPH RAG ===\n")
print("Entities Identified:", extracted_entities)
print("\nRetrieved Relationships:\n")
print(context)
print("Final Answer:\n")
print(response["message"]["content"])