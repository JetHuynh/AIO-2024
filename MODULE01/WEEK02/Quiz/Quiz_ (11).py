"""## Câu hỏi 11:(code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?bold text"""

# 11.abs_function
# Your code here : Tra ve gia tri trung binh cua list bang cach chia var cho so luong phan tu trong list_mums


def abs_function(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var / len(list_nums)


assert abs_function([4, 6, 8]) == 6
print("Quiz 11: ", abs_function())
