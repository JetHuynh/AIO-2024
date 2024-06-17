"""## Câu hỏi 5:(Code) Hoàn thành chương trình sau. Đầu ra của chương trình dưới đây là gì?"""

# 5.check_the_number


def check_the_number(num):
    list_of_numbers = []
    for i in range(1, 5):
        # Your code here
        # Su dung append them i vao trong list_of_number
        list_of_numbers.append(i)
    if num in list_of_numbers:
        results = "True"
    if num not in list_of_numbers:
        results = "False"
    return results


N = 7
assert check_the_number(N) == "False"

N = 2
results = check_the_number(N)
print("Quiz 05: ", results)
