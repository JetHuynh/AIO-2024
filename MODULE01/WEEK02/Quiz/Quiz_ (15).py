"""## Câu hỏi 15:(code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?"""

# 15.check_function


def function_helper(x):
    # Your code here
    if x > 0:
        return 'T'
    else:
        return 'N'
    # Neu x >0 tra ve ’T ’, nguoc lai tra ve ’N’


def check_function(data):
    res = [function_helper(x) for x in data]
    return res


data = [10, 0, -10, -1]
assert check_function(data) == ['T', 'N', 'N', 'N']
data = [2, 3, 5, -1]
print("Quiz 15: ", check_function(data))
