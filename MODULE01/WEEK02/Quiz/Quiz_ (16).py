"""## Câu hỏi 16:(code) Hãy hoàn thành chương trình dưới đây để loại bỏ những phần tử trùng nhau. Đầu ra của chương trình là gì?"""

# 16.distinct_function


def function_helper(x, data):
    for i in data:
        # Your code here
        # Neu x == i thi return 0
        if x == i:
            return 0
    return 1


def distinct_function(data):
    res = []
    for i in data:
        if function_helper(i, res):
            res.append(i)
    return res


lst = [10, 10, 9, 7, 7]
assert distinct_function(lst) == [10, 9, 7]
lst = [9, 9, 8, 1, 1]
print("Quiz 16: ", distinct_function(lst))
