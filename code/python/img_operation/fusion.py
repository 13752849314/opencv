# 图像的溶合
import cv2
import numpy as np

"""
api -> addWeighted(A, alpha, B, beta, gamma)
alpha, beta 为权重
gamma 静态权重
"""

img = cv2.imread(r'../../../image/test.png')
# print(img.shape)
back = np.zeros(img.shape, np.uint8)

result = cv2.addWeighted(img, 0.7, back, 0.3, 0)
cv2.imshow('add2', result)
cv2.waitKey(0)
