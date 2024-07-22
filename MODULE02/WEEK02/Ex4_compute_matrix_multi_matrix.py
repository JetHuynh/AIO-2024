"""## 1.4. Nhân ma trận với ma trận"""

# Multiplying a matrix by a matrix
import numpy as np
def compute_matrix_multi_matrix_(matrix1, matrix2):
    product = np.matmul(matrix1, matrix2)
    return product

def compute_matrix_multi_matrix(matrix1, matrix2):
    product = np.dot(matrix1, matrix2)
    return product

# example
matrix1 = np.array(range(10)).reshape(2,5)
matrix2 = np.array(range(10)).reshape(5,2)
result1 = compute_matrix_multi_matrix(matrix1, matrix2)
result2 = compute_matrix_multi_matrix_(matrix1, matrix2)
print(result1)
print(result2)