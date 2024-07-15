"""## Câu hỏi 12: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào phương pháp Lightness:"""

# Download image
#! gdown 1 i9dqan21DjQoG5Q_VEvm0LrVwAlXD0vB
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
img = mpimg.imread('Quiz\data\dog.jpeg')
'''
#Lightness: (max(R,G,B) + min(R,G,B))/2
#gray_img_01 = np.max(img, axis = 2)*0.5 + np.min(img, axis = 2)*0.5
#gray_img_01 = np.apply_along_axis(np.max, 2, img)*0.5 + np.apply_along_axis(np.min, 2, img)*0.5
'''
def lightness(vector):
    return (np.max(vector)*0.5 + np.min(vector)*0.5)

gray_img_01 = np.apply_along_axis(lightness, 2, img)

plt.imshow(gray_img_01, cmap = 'gray')
print(gray_img_01 [0, 0])