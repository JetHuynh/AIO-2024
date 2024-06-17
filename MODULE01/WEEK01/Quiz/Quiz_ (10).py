"""### Câu hỏi 10 : Dựa vào công thức xấp xỉ sin và điều kiện được giới thiệu các bạn click ở đây. Viết function xấp xỉ sin khi nhận x là giá trị muốn tính sin(x) và n là số lần lặp muốn xấp xỉ. Return về kết quả sin(x) với bậc xấp xỉ tương ứng. Đầu ra của chương trình sau đây là gì?"""
import math


def approx_sin(x, n):
    # Your code here
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    return result


# End your code
# assert round ( approx_sin (x=1, n =10) , 4) ==0.8415
print(round(approx_sin(x=3.14, n=10), 4))
