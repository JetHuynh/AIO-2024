"""# 2. Eigenvector và eigenvalues"""

# Eigenvector and eigenvalue
import numpy as np
def compute_eigenvalue_eigenvector(matrix):
    eigenvalue, eigenvector = np.linalg.eig(matrix)
    return eigenvalue, eigenvector

# example
matrix = np.array(range(9)).reshape(3,-1)
eigenvalue, eigenvector = compute_eigenvalue_eigenvector(matrix)
print(eigenvalue)
print('\n',eigenvector)

matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
eigenvalues, eigenvectors = compute_eigenvalue_eigenvector(matrix)
print('\n',eigenvectors)

"""# 3. Cosine Similarity"""