# Câu hỏi 1: Kết quả của đoạn code dưới đây là bao nhiêu.
import torch
import torch.nn as nn
data = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)
assert round(output[0].item(), 2)*100 == 9
print(output)
