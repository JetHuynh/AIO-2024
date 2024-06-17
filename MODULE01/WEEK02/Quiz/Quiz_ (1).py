"""## Câu hỏi 1:(Code) Hoàn thành chương trình sau với mô tả bài toán từ câu I.1. Đầu ra của chương trìnhdưới đây là gì?"""

# 1.max_kernel


def max_kernel(num_list, k):
    # Your Code Here
    result_list = []
    for i in range(len(num_list) - k + 1):
        max_num = max(num_list[i:i+k])
        result_list.append(max_num)
    return result_list
# End Code Here


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print("Quiz 01: ", max_kernel(num_list, k))
