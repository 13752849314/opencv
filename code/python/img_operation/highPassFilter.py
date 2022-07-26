# 高通滤波
"""
高通滤波最主要的作用是用于检测边缘
Sobel(索贝尔)（高斯），对噪声适应性强，很多算法均以索贝尔卷积核为基础
Scharr(沙尔)， 卷积核不会改变，3*3大小，如果Sobel(索贝尔)的size设为-1，则自动使用的则为沙尔滤波，所以一般情况下均使用索贝尔算法。
对于3*3的卷积核，Sobel(索贝尔)没有Scharr(沙尔)好，因为Scharr(沙尔)可以检测出更细的边缘线。Sobel(索贝尔)比较粗糙

缺点：计算边缘时，只能求一个方向，要么是横轴，要么是纵轴，最后再相加的出最终结果

Laplacian（拉普拉斯），优点不需要单独求x或y的边缘，可以直接将横轴和纵轴的边缘全部检测出来。
缺点：对噪声比较敏感，在其内部没有降噪的功能，因此在使用前，需要进行降噪处理。
"""

import cv2
import numpy as np

img = cv2.imread(r'../../../image/test.png')

"""
1. Sobel算子
api -> Sobel(src, ddepth, dx, dy, ksize=3, scale=1, delte=0, borderType=BORDER_DEFAULT)
"""

sobel1 = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel2 = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

sobel = cv2.add(sobel1, sobel2)

cv2.imshow('img', img)
# cv2.imshow('sobel1', sobel1)
# cv2.imshow('sobel2', sobel2)
# cv2.imshow('sobel', sobel)

"""
2. Scharr算子
api -> Scharr(src, ddepth, dx, dy, scale=1, delte=0, borderType=BORDER_DEFAULT)
"""

scharr1 = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharr2 = cv2.Scharr(img, cv2.CV_64F, 0, 1)

# scharr1 = cv2.Scharr(img, -1, 1, 0)
# scharr2 = cv2.Scharr(img, -1, 0, 1)

scharr = cv2.add(scharr1, scharr2)

# cv2.imshow('scharr1', scharr1)
# cv2.imshow('scharr2', scharr2)
# cv2.imshow('scharr', scharr)

"""
3. 拉普拉斯算子
api -> Laplacian(img, ddepth, ksize=1, scal =1, borderType=BORDER_DEFAULT)
"""

lap = cv2.Laplacian(img, -1, ksize=3)
cv2.imshow('lap', lap)
cv2.waitKey(0)
