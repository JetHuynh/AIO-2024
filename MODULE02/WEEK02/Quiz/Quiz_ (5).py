"""### 5. Kết quả của đoạn code sau đây là gì:"""

import numpy as np

from MODULE02.WEEK02.Ex3_compute_matrix_multi_vector import compute_matrix_multi_vector

m = np.array([[ -1 , 1, 1], [0, -4, 9]])
v = np.array([0 , 2, 1])
result = compute_matrix_multi_vector(m, v)
print(result)