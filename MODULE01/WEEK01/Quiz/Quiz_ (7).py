"""### Câu hỏi 7 : Viết function tính absolute error = |y −yˆ|. Nhận input là y và yˆ, return về kết quả absolute error tương ứng. Đầu ra của chương trình sau đây là gì?"""


def calc_ae(y, y_hat):
    # Your code here
    return abs(y - y_hat)


# End your code
y = 1
y_hat = 6
assert calc_ae(y, y_hat) == 5
y = 2
y_hat = 9
print(calc_ae(y, y_hat))
