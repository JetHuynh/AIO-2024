"""## Câu hỏi 15: Lấy giá trị lớn nhất và chỉ mục tương ứng của nó trên cột Sales:"""

import pandas as pd
df = pd.read_csv('Quiz\data\Advertising.csv')
data = df.to_numpy()
print(f'Max: {data[:,3].max()} - Index: {data[:,3].argmax()}')