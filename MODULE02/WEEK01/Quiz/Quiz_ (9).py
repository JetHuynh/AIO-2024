
"""## Câu hỏi 9: Kết quả của đoạn code sau đây:"""

import numpy as np
a = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.where((a >= 5) & (a <= 10))
print("result", a[index])
