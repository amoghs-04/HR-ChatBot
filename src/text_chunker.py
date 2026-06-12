# src/text_chunker.py

def chunk_documents(pages, chunk_size=500, overlap=100):

    chunks = []

    for page in pages:

        text = page["text"]
        page_num = page["page"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk = text[start:end]

            chunks.append({
                "text": chunk,
                "page": page_num
            })

            start += chunk_size - overlap

    return chunks