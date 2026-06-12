from src.pdf_loader import load_pdf
from src.text_chunker import chunk_documents
from src.embeddings import generate_embeddings
from src.vector_db import create_faiss_index, save_index

pages = load_pdf("data/HR-Policy-Manual-Template (1).pdf")

chunks = chunk_documents(
    pages,
    chunk_size=500,
    overlap=100
)

embeddings = generate_embeddings(chunks)

index = create_faiss_index(embeddings)

save_index(index, chunks)

print("FAISS Index Saved Successfully!")
print("Total Chunks:", len(chunks))