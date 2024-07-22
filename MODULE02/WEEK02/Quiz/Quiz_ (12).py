"""### 12. Kết quả của đoạn code sau đây là gì:"""

import numpy as np

from MODULE02.WEEK02.Ex7_compute_cosine_similarity import compute_cosine_similarity

x = np.array([1 , 2, 3, 4])
y = np.array([1 , 0, 3, 0])
result = compute_cosine_similarity(x,y)
print(round(result, 3))