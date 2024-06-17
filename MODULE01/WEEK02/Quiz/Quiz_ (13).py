"""## Câu hỏi 13:(code) Hãy hoàn thành chương trình sau đây thực hiện tính giai thừa của 1 số. Đầu ra của chương trình dưới đây là gì?"""

# 13.factorial_function


def factorial_function(y):
    var = 1
    while (y > 1):
        # Your code here
        var *= y
        y -= 1
    return var


assert factorial_function(8) == 40320
print("Quiz 13: ", factorial_function(4))
