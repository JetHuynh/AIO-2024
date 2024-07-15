"""## Câu hỏi 19: Tính tổng các hàng của cột Sales với điều kiện giá trị Newspaper lớn hơn giá trị trung bình của cột Newspaper:"""

import pandas as pd
df = pd.read_csv('Quiz\data\Advertising.csv')
data = df.to_numpy()

print(f'Sum: {data[data[:,2] > data[:,2].mean(),3].sum()}')
# print(f'Sum: {data[data[:,2] > data[:,2].mean()][:,3].sum()}')
