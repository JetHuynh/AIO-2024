"""## Câu hỏi 16: Giá trị trung bình của cột TV là:"""

import pandas as pd
df = pd.read_csv('Quiz\data\Advertising.csv')
data = df.to_numpy()
print(f'AVG: {data[:,0].mean()}')