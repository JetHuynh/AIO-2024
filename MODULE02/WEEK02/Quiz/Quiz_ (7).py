"""### 7. Kết quả của đoạn code sau đây là gì:"""

import numpy as np

m1 = np.eye(3)
m2 = np.array([[1 , 1, 1] ,[2 , 2, 2], [3, 3, 3]])
result = m1@m2
print(result)