"""### 8. Kết quả của đoạn code sau đây là gì:"""

import numpy as np

m1 = np.eye(2)
m1 = np.reshape(m1 ,( -1 ,4))[0]
m2 = np.array([[1 , 1, 1, 1] ,[2 , 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1@m2
print(result)