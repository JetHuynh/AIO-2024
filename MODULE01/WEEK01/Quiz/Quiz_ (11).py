"""### Câu hỏi 11 : Dựa vào công thức xấp xỉ sinh và điều kiện được giới thiệu các bạn click ở đây. Viếtfunction xấp xỉ sinh khi nhận x là giá trị muốn tính sinh(x) và n là số lần lặp muốn xấp xỉ. Return vềkết quả sinh(x) với bậc xấp xỉ tương ứng. Đầu ra của chương trình sau đây là gì?"""
import math


def approx_sinh(x, n):
    # Your code here
    result = 0
    for i in range(n):
        result += (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    return result


# End your code
# assert round ( approx_sinh (x=1, n =10) , 2) ==1.18
print(round(approx_sinh(x=3.14, n=10), 2))
