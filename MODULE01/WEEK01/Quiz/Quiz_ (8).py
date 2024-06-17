"""### Câu hỏi 8 : Viết function tính squared error = (y−yˆ)2. Nhận input là y và yˆ, return về kết quả squared error tương ứng. Đầu ra của chương trình sau đây là gì?"""


def calc_se(y, y_hat):
    # Your code here
    return (y - y_hat) ** 2


# End your code
y = 4
y_hat = 2
assert calc_se(y, y_hat) == 4
print(calc_se(2, 1))
