"""### 11. Kết quả của đoạn code sau đây là gì:"""

import numpy as np

from MODULE02.WEEK02.Ex6_compute_eigenvalue_eigenvector import compute_eigenvalue_eigenvector

matrix = np.array([[0.9 , 0.2] , [0.1 , 0.8]])
eigenvalues , eigenvectors = compute_eigenvalue_eigenvector(matrix)
print(eigenvectors)