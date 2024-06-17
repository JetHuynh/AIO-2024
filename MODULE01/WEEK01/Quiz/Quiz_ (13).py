"""### Câu hỏi 13 : Đoạn code nào thực hiện đúng Mean Difference of nth Root Error được miêu tả ở trên?"""

# (A)


def md_nre_single_sample(y, y_hat, n, p):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss
# (B)


def md_nre_single_sample1(y, y_hat, n, p):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/2)  # wrong >>1/n
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss
# (C)


def md_nre_single_sample2(y, y_hat, n, p):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)
    difference = y_root / y_hat_root  # wrong >> y-y_hat
    loss = difference ** p
    return loss
# (D)


def md_nre_single_sample3(y, y_hat, n):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)
    difference = y_root - y_hat_root
    loss = difference  # wrong >>diff**p
    return loss


print('A')
