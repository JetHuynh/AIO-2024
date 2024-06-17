"""## Câu hỏi 7:(code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?"""

# 7.extend_function


def extend_function(x, y):
    # Your code here
    # Su dung extend de noi y vao x
    x.extend(y)
    return x


list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]
assert extend_function(list_num1, extend_function(
    list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]
list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]
print("Quiz 07: ", extend_function(
    list_num1, extend_function(list_num2, list_num3)))
