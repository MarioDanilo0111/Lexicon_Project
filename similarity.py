import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity

def get_embedding(query):
    # This function needs to convert the query to an embedding
    return np.random.normal(size=(768,))  # Embedding has 768 dimension

def find_most_similar_embeddings(query_embedding, data_embeddings, top_k=5):
    # Calculate cosine similarity
    similarities = cosine_similarity([query_embedding], data_embeddings)
    # Get the indices of the top_k most similar embeddings
    top_indices = np.argsort(similarities[0])[::-1][:top_k]
    
    # Return the top_k most similar embeddings
    return top_indices, similarities[0][top_indices]