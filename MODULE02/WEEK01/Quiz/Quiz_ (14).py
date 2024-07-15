"""## Câu hỏi 14: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào phương pháp Luminosity:"""

# Download image
#! gdown 1 i9dqan21DjQoG5Q_VEvm0LrVwAlXD0vB
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
img = mpimg.imread('Quiz\data\dog.jpeg')
'''
#Luminosity: 0.21*R + 0.72*G + 0.07*B
#gray_img_03 = 0.21*img[:,:,0] + 0.72*img[:,:,1] + 0.07*img[:,:,2]
#gray_img_03 = np.apply_along_axis(lambda x: 0.21*x[0] + 0.72*x[1] + 0.07*x[2], 2, img)
#gray_img_03 = np.dot(img[...,:3], [0.21, 0.72, 0.07])
#gray_img_03 = np.sum(img*np.array([0.21, 0.72, 0.07]), axis = 2)
'''
def luminosity(vector):
    return 0.21*vector[0] + 0.72*vector[1] + 0.07*vector[2]

gray_img_03 = np.apply_along_axis(luminosity, 2, img)

plt.imshow(gray_img_03, cmap = 'gray')
print(gray_img_03 [0, 0])