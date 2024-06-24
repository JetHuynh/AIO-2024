"""## Câu hỏi 2: Hoàn thành đoạn code sau đây theo công thức tính softmax."""

import torch
import torch .nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        # Your Code Here
        return torch.exp(x) / torch.exp(x).sum()
        # End Code Here


data = torch.Tensor([5, 2, 4])
my_softmax = MySoftmax()
output = my_softmax(data)
assert round(output[-1].item(), 2)*100 == 26
print(output)
