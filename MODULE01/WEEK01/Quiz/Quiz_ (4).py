"""### Câu hỏi 4 : Viết function thực hiện Sigmoid Function f(x) = 1/(1 + e^−x). Nhận input là x và return kết quả tương ứng trong Sigmoid Function. Đầu ra của chương trình sau đây là gì?"""

import math
def calc_sig (x):
# Your code here
    return 1 / (1 + math.exp(-x))
# End your code
assert round ( calc_sig (3) , 2) ==0.95
print ( round ( calc_sig (2) , 2))