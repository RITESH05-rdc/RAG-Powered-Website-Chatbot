import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_vector_store(chunks):

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    faiss.write_index(index, "vector_store/index.faiss")

    with open("vector_store/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

def search(query):

    index = faiss.read_index("vector_store/index.faiss")

    with open("vector_store/chunks.pkl","rb") as f:
        chunks = pickle.load(f)

    query_vector = model.encode([query])

    D, I = index.search(query_vector, 3)

    results = [chunks[i] for i in I[0]]

    return results

import requests

def ask_llm(prompt):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]