"""## Câu hỏi 4:(Code) Hoàn thành chương trình sau với mô tả bài toán từ câu I.4. Đầu ra của chương trìnhdưới đây là gì?"""

# 4.levenshtein_distance


def levenshtein_distance(token1, token2):
    # Your Code Here
    m = len(token1)  # số dòng
    n = len(token2)  # số cột
    # 1.khai báo ma trận lưu trữ(m+1 x n+1)
    distance = [[0] * (n + 1) for _ in range(m + 1)]
    # 2.1.hoàn thiện cột đầu tiên(0-m)
    for i in range(m + 1):
        distance[i][0] = i
    # 2.2.hoàn thiện dòng đầu tiên (0-n)
    for j in range(n + 1):
        distance[0][j] = j
    # 3.hoàn thiện các ô còn lại
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if token1[i - 1] == token2[j - 1]:
                sub_unit = 0
            else:
                sub_unit = 1
            sub_cost = distance[i - 1][j - 1] + sub_unit
            insert_cost = distance[i][j - 1] + 1
            delete_cost = distance[i - 1][j] + 1
            distance[i][j] = min(sub_cost, insert_cost, delete_cost)
    # 4.trả về giá trị ô cuối cùng
    return distance[m][n]

# End Code Here


assert levenshtein_distance("hi", "hello") == 4
print("Quiz 04: ", levenshtein_distance("hola", "hello"))
