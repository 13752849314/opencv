# 图像的位运算
import cv2
import numpy as np

"""
1. 非运算
api -> bitwise_not(img)
"""

img = cv2.imread(r'../../../image/test.png')

result1 = cv2.bitwise_not(img)

cv2.imshow('result1', result1)

"""
2. 与运算
api -> bitwise_and(img1, img2)
"""
img2 = np.zeros(img.shape, np.uint8)
img2[50:500, 50:500] = 255
cv2.imshow('img2', img2)
result2 = cv2.bitwise_and(img, img2)
cv2.imshow('result2', result2)

"""
3. 或运算与异或运算
api -> bitwise_or(img1, img2)
api -> bitwise_xor(img1, img2)
"""
result3 = cv2.bitwise_or(img, img2)
result4 = cv2.bitwise_or(img, img2)
cv2.imshow('result3', result3)
cv2.imshow('result4', result4)
cv2.waitKey(0)
