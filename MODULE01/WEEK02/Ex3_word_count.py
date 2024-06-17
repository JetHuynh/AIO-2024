# 3.file - Word count
def word_count(file_path):
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


file_path = 'MODULE01\WEEK02\P1_data.txt'
print(word_count(file_path))
