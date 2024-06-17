
# 1.num_list - max_sliding_window
def max_sliding_window(num_list, k):
    result_list = []
    for i in range(len(num_list) - k + 1):
        max_num = max(num_list[i:i+k])
        result_list.append(max_num)
    return result_list


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_sliding_window(num_list, k))
