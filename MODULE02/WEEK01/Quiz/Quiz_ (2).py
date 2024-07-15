"""## Câu hỏi 2: Cách tạo một mảng boolean 3x3 với tất cả giá trị là True"""
import numpy as np
arr = np.ones((3 ,3)) > 0
print(arr)

arr = np.ones((3 ,3), dtype = bool)
print(arr)

arr = np.full((3 ,3), fill_value =True, dtype = bool)
print(arr)

print('All ok')