# circumscribed rectangle 外接矩形

import cv2
import numpy as np

img = cv2.imread(r'../../../image/flash.png')
cv2.imshow('img', img)

# 灰度图
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv2.threshold(grey, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', binary)

# 轮廓查找
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 1. 最小外接矩阵
min_rect = cv2.minAreaRect(contours[0])
print(min_rect)
box = cv2.boxPoints(min_rect)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

# 2. 最大外接矩阵
max_rect = cv2.boundingRect(contours[0])
print(max_rect)
x, y, w, h = max_rect
cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 2), 2)

cv2.imshow('min', img)
cv2.waitKey(0)
