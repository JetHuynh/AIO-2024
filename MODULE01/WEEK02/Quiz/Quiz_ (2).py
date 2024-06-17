"""## Câu hỏi 2:(Code) Hoàn thành chương trình sau với mô tả bài toán từ câu I.2. Đầu ra của chương trìnhdưới đây là gì?"""

# 2.character_count


def character_count(word):
    # Your Code Here
    result = {}
    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
# End Code Here


assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print("Quiz 02: ", character_count('smiles'))
