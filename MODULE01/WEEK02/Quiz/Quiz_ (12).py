"""## Câu hỏi 12:(code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình dưới đây là gì?"""

# 12.modulo_function


def modulo_function(data):
    var = []
    for i in data:
        # Your code here
        if i % 3 == 0:
            var.append(i)
    # Neu i chia het cho 3 thi them i vao list var
    return var


assert modulo_function([3, 9, 4, 5]) == [3, 9]
print("Quiz 12: ", modulo_function([1, 2, 3, 5, 6]))
