"""## Câu hỏi 20: Gọi giá trị trung bình của cột Sales là A. Tạo ra mảng mới scores chứa các giá trị Good, Average và Bad sao cho: nếu giá trị hiện tại > A => giá trị trong mảng mới là Good, < A thì sẽ là Bad và = A sẽ là Average. Sau đó in ra kết quả scores[7:10]"""

import numpy as np
import pandas as pd
df = pd.read_csv('Quiz\data\Advertising.csv')
data = df.to_numpy()

A = data[:,3].mean()
scores = np.where(data[:,3] > A, 'Good', np.where(data[:,3] < A, 'Bad', 'Average'))
print(scores[7:10])