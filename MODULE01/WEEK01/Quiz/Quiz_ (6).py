"""### Câu hỏi 6 : Viết function nhận 2 giá trị x, và tên của activation function act_name activationfunction chỉ có 3 loại (sigmoid, relu, elu), thực hiện tính toán activation function tương ứng vớiname nhận được trên giá trị của x và trả kết quả. Đầu ra của chương trình sau đây là gì?"""

import math


def calc_activation_func(x, act_name):
    # Your code here
    if act_name == 'sigmoid':
        return 1 / (1 + math.exp(-x))
    elif act_name == 'relu':
        return max(0, x)


# End your code
assert calc_activation_func(x=1, act_name='relu') == 1
print(round(calc_activation_func(x=3, act_name='sigmoid'), 2))
