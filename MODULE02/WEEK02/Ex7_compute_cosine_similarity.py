# Cosine Similarity
import numpy as np

from Ex1_compute_vector_length import compute_vector_length
from Ex2_compute_dot_product import compute_dot_product

def compute_cosine_similarity_tradition(vector1, vector2):
    cosine_similarity = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    return cosine_similarity

def compute_cosine_similarity(vector1, vector2):
    cosine_similarity = compute_dot_product(vector1, vector2) / (compute_vector_length(vector1) * compute_vector_length(vector2))
    return cosine_similarity

# example
vector1 = np.array(range(10))
vector2 = np.array(range(0,50,5))
result1 = compute_cosine_similarity_tradition(vector1, vector2)
result2 = compute_cosine_similarity(vector1, vector2)
print(result1)
print(result2)