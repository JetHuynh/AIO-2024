"""### 2. Kết quả của đoạn code sau đây là gì:"""

import numpy as np
from MODULE02.WEEK02.Ex2_compute_dot_product import compute_dot_product
v1 = np.array([0 , 1, -1, 2])
v2 = np.array([2 , 5, 1, 0])
result = compute_dot_product (v1 , v2)
print(round(result ,2))