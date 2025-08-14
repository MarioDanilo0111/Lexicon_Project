import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load the pre-trained sentence-transformers model
model = SentenceTransformer('all-MiniLM-L6-v2')

# This replaces the old fake SHA256-based embedding function
def get_embedding(query):
    return model.encode(query)

# This function remains mostly the same
def find_most_similar_embeddings(query_embedding, data_embeddings, top_k=5):
    # Calculate cosine similarity
    similarities = cosine_similarity([query_embedding], data_embeddings)
    # Get the indices of the top_k most similar embeddings
    top_indices = np.argsort(similarities[0])[::-1][:top_k]
    # Return the top_k most similar embeddings
    return top_indices, similarities[0][top_indices]
