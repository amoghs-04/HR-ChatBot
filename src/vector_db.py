import faiss
import numpy as np
import pickle


def create_faiss_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index


def save_index(index, chunks):

    faiss.write_index(index, "vector_store/hr_policy.index")

    with open("vector_store/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)


def load_index():

    index = faiss.read_index("vector_store/hr_policy.index")

    with open("vector_store/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    return index, chunks