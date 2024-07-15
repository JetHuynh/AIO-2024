"""## Câu hỏi 13: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào phương pháp Average:"""

# Download image
#! gdown 1 i9dqan21DjQoG5Q_VEvm0LrVwAlXD0vB
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
img = mpimg.imread('Quiz\data\dog.jpeg')
'''
#Average: (R+G+B)/3
#gray_img_02 = np.mean(img, axis = 2)
#gray_img_02 = np.apply_along_axis(np.mean, 2, img)
#gray_img_02 = np.sum(img, axis = 2)/3
'''
def average(vector):
    return np.sum(vector)/3

gray_img_02 = np.apply_along_axis(average, 2, img)

plt.imshow(gray_img_02, cmap = 'gray')
print(gray_img_02 [0, 0])