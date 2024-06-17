"""## Câu hỏi 3:(Code) Hoàn thành chương trình sau với mô tả bài toán từ câu I.3. Đầu ra của chương trìnhdưới đây là gì?"""

# 3.count_word
#!gdown https :// drive . google .com/uc?id =1 IBScGdW2xlNsc9v5zSAya548kNgiOrko


def count_word(file_path):
    # Your Code Here
    with open(file_path, 'r') as file_object:
        file_content = file_object.read()  # load nội dung file
        # xử lý - chuyển tấc cả các từ sang chữ thường
        file_content = file_content.lower()
    list_word = file_content.split()  # băm chuỗi nội dung thành một list
    dict_count = {}  # khai báo dictionary trả về
    for word in list_word:
        if word in dict_count:
            dict_count[word] += 1
        else:
            dict_count[word] = 1

    # sắp xếp lại dictionary
    dict_count = dict(sorted(dict_count.items(), key=lambda x: x[0]))
    return dict_count
# End Code Here


file_path = 'MODULE01\WEEK02\P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print("Quiz 03: ", result['man'])
