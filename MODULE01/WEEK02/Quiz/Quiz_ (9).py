"""## Câu hỏi 9:(code) Hãy hoàn thành chương trình tìm phần tử có giá trị lớn nhất trong một list dưới đây. Đầu ra của chương trình là gì?"""

# 9.max_function


def max_function(n):
    # Your code here
    max_value = max(n)
    return max_value


my_list = [1001, 9, 100, 0]
assert max_function(my_list) == 1001
my_list = [1, 9, 9, 0]
print("Quiz 09: ", max_function(my_list))
