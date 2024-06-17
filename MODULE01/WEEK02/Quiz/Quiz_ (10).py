"""## Câu hỏi 10:(code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?"""

# 10.compare_function
# Thuc hien duyet tung phan tu trong integers , so sanh tung phan tu voi number , neu bang nhau tra ve True , khac nhau tra ve false
# vi du: integers = [1, 2, 3], number = 2, ban se tao ra list [False , True , False ]


def compare_function(integers, number=1):
    result = []
    for i in integers:
        if i == number:
            result.append(True)
        else:
            result.append(False)
    return any(result)


my_list = [1, 3, 9, 4]
assert compare_function(my_list, -1) == False
my_list = [1, 2, 3, 4]
print("Quiz 10: ", compare_function(my_list, 2))
