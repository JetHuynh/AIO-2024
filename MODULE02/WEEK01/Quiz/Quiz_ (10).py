"""## Câu hỏi 10: Kết quả của đoạn code sau đây:"""

import numpy as np
def maxx(x,y):
    if x >= y:
        return x
    else:
        return y
a = np.array([5,7,9,8,6,4,5])
b = np.array([6,3,4,8,9,7,1])
pair_max = np.vectorize(maxx,otypes =[float])
print(pair_max(a,b))