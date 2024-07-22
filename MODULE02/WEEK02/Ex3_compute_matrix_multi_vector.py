"""## 1.3. Nhân vector với ma trận"""

# Multiplying a vector by a matrix
import numpy as np
def compute_matrix_multi_vector(matrix, vector):    
    product = np.dot(matrix, vector)
    return product

def compute_matrix_multi_vector_(matrix, vector):
    product = matrix.dot(vector)
    return product

# example
matrix = np.array(range(100)).reshape(10,10)
vector = np.array(range(10))
result1 = compute_matrix_multi_vector(matrix, vector)
result2 = compute_matrix_multi_vector_(matrix, vector)
print(result1)
print(result2)