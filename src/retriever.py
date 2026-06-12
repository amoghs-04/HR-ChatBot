from sentence_transformers import SentenceTransformer
from src.vector_db import load_index

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_chunks(query, k=3):

    index, chunks = load_index()

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, k)

    results = []

    for idx in indices[0]:
        results.append(chunks[idx])

    return results