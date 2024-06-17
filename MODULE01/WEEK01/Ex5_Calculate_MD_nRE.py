"""## 5. Viết function thực hiện Mean Difference of n^th Root Error"""
# calculate MD_nRE


def calculate_md_nre(y, y_hat, n, p):
    result = ((y ** (1 / n)) - (y_hat ** (1 / n))) ** p
    print(f'MD_nRE: {result}')


# RunExample
calculate_md_nre(100, 99.5, 2, 1)
calculate_md_nre(50, 49.5, 2, 1)
calculate_md_nre(20, 19.5, 2, 1)
calculate_md_nre(0.6, 0.1, 2, 1)
