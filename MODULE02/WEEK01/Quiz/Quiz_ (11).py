"""## Câu hỏi 11: Kết quả của đoạn code sau đây:"""

import numpy as np
a = np.array([5,7,9,8,6,4,5])
b = np.array([6,3,4,8,9,7,1])
print("Result",np.where(a<b, b, a))