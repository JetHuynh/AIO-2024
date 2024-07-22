"""# Câu hỏi trắc nghiệm

### 1. Kết quả của đoạn code sau đây là gì:
"""

import numpy as np

from MODULE02.WEEK02.Ex1_compute_vector_length import compute_vector_length

vector = np.array([-2, 4, 9, 21])
result = compute_vector_length([vector])
print (round(result,2))