"""### 6. Kết quả của đoạn code sau đây là gì:"""

import numpy as np

from MODULE02.WEEK02.Ex4_compute_matrix_multi_matrix import compute_matrix_multi_matrix

m1 = np.array([[0 , 1, 2], [2, -3, 1]])
m2 = np.array([[1 , -3] ,[6 , 1], [0, -1]])
result = compute_matrix_multi_matrix(m1 , m2)
print(result )