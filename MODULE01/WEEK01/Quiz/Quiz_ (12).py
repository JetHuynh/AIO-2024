"""
### Câu hỏi 12 : Dựa vào công thức xấp xỉ cosh và điều kiện được giới thiệu các bạn click ở đây. Viết function xấp xỉ cosh khi nhận x là giá trị muốn tính cosh(x) và n là số lần lặp muốn xấp xỉ. Return về kết quả cosh(x) với bậc xấp xỉ tương ứng. Đầu ra của chương trình sau đây là gì?"""
import math


def approx_cosh(x, n):
    # Your code here
    result = 0
    for i in range(n):
        result += (x ** (2 * i)) / math.factorial(2 * i)
    return result


# End your code
# assert round(approx_cosh(x=1, n=10), 2) == 1.54
print(round(approx_cosh(x=3.14, n=10), 2))
