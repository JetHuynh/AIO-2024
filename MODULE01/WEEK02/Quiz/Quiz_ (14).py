"""## Câu hỏi 14:(code) Hãy hoàn thành chương trình đảo ngược chuỗi dưới đây. Đầu ra của chương trình là gì?"""

# 14.reverse_function


def reverse_function(x):
    # your code here
    return x[::-1]


x = 'I can do it'
assert reverse_function(x) == "ti od nac I"
x = 'apricot'
print("Quiz 14: ", reverse_function(x))
