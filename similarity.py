import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity
import hashlib

def get_embedding(query):
     # Deterministic embedding generation using a hash function
    hash_object = hashlib.sha256(query.encode())
    hash_digest = hash_object.digest()
    embedding = np.frombuffer(hash_digest, dtype=np.uint8)[:768] / 255.0  # Normalize to 0-1 range
    embedding = embedding.astype(np.float32)

    # Ensure the embedding has 768 dimensions by padding if necessary
    if len(embedding) < 768:
        padding = np.zeros(768 - len(embedding), dtype=np.float32)
        embedding = np.concatenate((embedding, padding))
    return embedding

def find_most_similar_embeddings(query_embedding, data_embeddings, top_k=5):
    # Calculate cosine similarity
    similarities = cosine_similarity([query_embedding], data_embeddings)
    # Get the indices of the top_k most similar embeddings
    top_indices = np.argsort(similarities[0])[::-1][:top_k]
    
    # Return the top_k most similar embeddings
    return top_indices, similarities[0][top_indices]