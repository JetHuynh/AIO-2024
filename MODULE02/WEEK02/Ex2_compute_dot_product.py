"""## 1.2. Phép tích vô hướng"""

# Dot product
import numpy as np
def compute_dot_product_tradition(vector1, vector2):
    dot_product = np.sum(vector1 * vector2)
    return dot_product

def compute_dot_product(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    return dot_product

# example:
vector1 = np.array(range(10))
vector2 = np.array(range(10,20))
result1 = compute_dot_product_tradition(vector1, vector2)
result2 = compute_dot_product(vector1, vector2)
print(result1)
print(result2)