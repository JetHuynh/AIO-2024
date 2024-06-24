import torch
import torch.nn as nn

# Class Softmax


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return (torch.exp(x) / torch.exp(x).sum())


# Class SoftmaxStable


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return (torch.exp(x - torch.max(x)) / torch.exp(x - torch.max(x)).sum())


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(f'Softmax: {output}')

data_stable = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output_stable = softmax_stable(data_stable)
print(f'Softmax_stable: {output_stable}')
