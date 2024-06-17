"""## Câu hỏi 6:(Code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?"""

# 6.append_function


def append_function(data, max, min):
    result = []
    for i in data:
        # Your code here
        # Neu i < min thi them min vao result
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


my_list = [5, 2, 5, 0, 1]
max = 1
min = 0
assert append_function(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
my_list = [10, 2, 5, 0, 1]
max = 2
min = 1
print("Quiz 06: ", append_function(max=max, min=min, data=my_list))
