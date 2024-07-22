"""### 10. Kết quả của đoạn code sau đây là gì:"""

import numpy as np

from MODULE02.WEEK02.Ex5_compute_matrix_inverse import compute_matrix_inverse
m1 = np.array([[ -2 , 6], [8, -4]])
result = compute_matrix_inverse(m1)
print(result)