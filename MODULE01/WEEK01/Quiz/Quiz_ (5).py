"""### Câu hỏi 5 : Viết function thực hiện Elu Function. Nhận input là x vàreturn kết quả tương ứng trong Elu Function. Đầu ra của chương trình sau đây là gì khi α = 0.01?"""

import math
def calc_elu (x):
# Your code here
    alpha = 0.01
    return alpha * (math.exp(x) - 1) if x < 0 else x
# End your code
assert round ( calc_elu (1))==1
print ( round ( calc_elu ( -1) , 2))