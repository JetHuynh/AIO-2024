"""### Câu hỏi 9 : Dựa vào công thức xấp xỉ cos và điều kiện được giới thiệu các bạn click ở đây. Viết function xấp xỉ cos khi nhận x là giá trị muốn tính cos(x) và n là số lần lặp muốn xấp xỉ. Return về kết quả cos(x) với bậc xấp xỉ tương ứng. Đầu ra của chương trình sau đây là gì?"""
import math


def approx_cos(x, n):
    # Your code here
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    return result


# End your code
# assert round ( approx_cos (x=1, n =10) , 2) ==0.54
print(round(approx_cos(x=3.14, n=10), 2))
