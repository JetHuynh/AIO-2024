
"""## 1.1. Độ dài của vector"""

#Length of a vector
import numpy as np
def compute_vector_length_tradition(vector):
    lenvector = np.sqrt(np.sum(np.square(vector)))
    return lenvector

def compute_vector_length(vector):
    lenvector = np.linalg.norm(vector)
    return lenvector

# example:
vector = np.array(range(10))
result1 = compute_vector_length([vector])
result2 = compute_vector_length_tradition([vector])
print(result1)
print(result2)