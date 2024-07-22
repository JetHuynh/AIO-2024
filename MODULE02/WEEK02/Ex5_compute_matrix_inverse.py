"""## 1.5. Ma trận nghịch đảo"""

# Matrix inverse
import numpy as np
def compute_matrix_inverse(matrix):
    inverse = np.linalg.inv(matrix)
    return inverse

# example
matrix = np.array(range(4)).reshape(2,2)
result = compute_matrix_inverse(matrix)
print(result)

m1 = np.array([[-2, 6], [8, -4]])
result = compute_matrix_inverse(m1)
print(result)