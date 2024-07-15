"""## Câu hỏi 18: Tính giá trị trung bình của cột Radio thoả mãn điều kiện giá trị tương ứng trên cột Sales lớn hơn hoặc bằng 15:"""

import pandas as pd
df = pd.read_csv('Quiz\data\Advertising.csv')
data = df.to_numpy()
print(f'AVG: {data[data[:,3] >= 15,1].mean()}')
#print(f'AVG: {data[data[:,3] >= 15][:,1].mean()}')