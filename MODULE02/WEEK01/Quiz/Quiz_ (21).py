"""## Câu hỏi 21: Gọi giá trị trên cột Sales gần nhất với giá trị trung bình cũng chính cột Sales là A. Tạo ra mảng mới scores chứa các giá trị Good, Average và Bad sao cho: nếu giá trị hiện tại > A => giá trị trong mảng mới là Good, < A thì sẽ là Bad và = A sẽ là Average. Sau đó in ra kết quả scores[7:10]"""

import numpy as np
import pandas as pd
df = pd.read_csv('Quiz\data\Advertising.csv')
data = df.to_numpy()
A = data[:,3].mean()
#Giá trị gần nhất với A
index = np.abs(data[:,3] - A).argmin()
near_A = data[index,3]
scores = np.where(data[:,3] > near_A, 'Good', np.where(data[:,3] < near_A, 'Bad', 'Average'))
print(scores[7:10])