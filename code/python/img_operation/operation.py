import cv2
import numpy as np

img = cv2.imread(r'../../../image/test.png')

# print(img.shape)

img1 = np.ones((800, 1280, 3), np.uint8) * 50

cv2.imshow('orig', img)
result = cv2.add(img, img1)  # +
result1 = cv2.subtract(img, img1)  # -
result2 = cv2.multiply(img, img1)  # *
result3 = cv2.divide(img, img1)  # /

cv2.imshow('add_result', result)
cv2.imshow('sub_result', result1)
cv2.imshow('mut_result', result2)
cv2.imshow('div_result', result3)
cv2.waitKey(0)
