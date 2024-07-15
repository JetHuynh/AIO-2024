"""# Câu hỏi 17: Số lượng bản ghi có giá trị tại cột Sales lớn hơn hoặc bằng 20 là:"""

import pandas as pd
df = pd.read_csv('Quiz\data\Advertising.csv')
data = df.to_numpy()
'''
#print(f'Count: {data[data[:,3] >= 20].shape[0]}')
#print(f'Count: {len(data[data[:,3] >= 20])}')
'''
print(f'Count: {sum(data[:,3] >= 20)}')