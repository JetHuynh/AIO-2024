"""# 4. Background subtraction"""
"""## Resize các ảnh đầu vào về cùng kích thước"""

# Resize các ảnh đầu vào về cùng kích thước

import numpy as np
import cv2
bg1_image = cv2.imread('MODULE02\WEEK02\Image data\GreenBackground.png', 1)
ob_image = cv2.imread('MODULE02\WEEK02\Image data\Object.png', 1)
bg2_image = cv2.imread('MODULE02\WEEK02\Image data\\NewBackground.jpg', 1)

bg1_image = cv2.resize(bg1_image, (678, 381))
ob_image = cv2.resize(ob_image, (678, 381))
bg2_image = cv2.resize(bg2_image, (678, 381))
cv2.imshow('background', bg1_image,)
cv2.imshow('object', ob_image)
cv2.imshow('newbackground', bg2_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""## Xây dựng hàm compute_difference"""

# Xây dựng hàm compute_difference


def compute_difference(bg_img, input_img):
    difference_three_channel = cv2.absdiff(bg_img, input_img)
    '''# difference_single_channel = cv2.cvtColor(difference_three_channel, cv2.COLOR_BGR2GRAY)'''
    difference_single_channel = np.sum(difference_three_channel, axis=2) / 3.0
    difference_single_channel = difference_single_channel.astype('uint8')
    return difference_single_channel


difference_single_channel = compute_difference(bg1_image, ob_image)
cv2.imshow('difference_single_channel', difference_single_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""# Xây dựng hàm compute_binary_mask"""
# Xây dựng hàm compute_binary_mask


def compute_binary_mask(difference_single_channel):
    '''# _, binary_mask = cv2.threshold(difference_single_channel, 10, 255, cv2.THRESH_BINARY)'''
    binary_mask = np.where(difference_single_channel > 10, 255, 0)
    binary_mask = np.stack((binary_mask,)*3, axis=-1)
    binary_mask = binary_mask.astype('uint8')
    return binary_mask


binary_mask = compute_binary_mask(difference_single_channel)
cv2.imshow('binary_mask', binary_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""## Xây dựng hàm replace_background"""

# Xây dựng hàm replace_background


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)
    replaced_img = np.where(binary_mask == 255, ob_image, bg2_image)

    return replaced_img


output = replace_background(bg1_image, bg2_image, ob_image)
cv2.imshow('replaced_background', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
