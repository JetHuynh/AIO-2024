"""## Câu hỏi 8:(code) Hãy hoàn thành chương trình tìm phần tử có giá trị nhỏ nhất trong một list dướiđây. Đầu ra của chương trình là gì?"""

# 8.min_function


def min_function(n):
    # Your code here
    min_value = min(n)
    return min_value


my_list = [1, 22, 93, -100]
assert min_function(my_list) == -100
my_list = [1, 2, 3, -1]
print("Quiz 08: ", min_function(my_list))
