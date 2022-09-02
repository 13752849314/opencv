# 图像滤波
import cv2
import numpy as np

img = cv2.imread(r'../../../image/test.png')
cv2.imshow('img', img)
"""
低通滤波可以去除噪声或平滑图像
高通滤波可以帮助查找图像的边缘

图像卷积
api -> filter2D(src, ddepth, kernel, anchor, delta, borderType)
@:param ddepth 位深
@:param kernel 卷积核
@:param anchor 锚点
@:param delta 
@:param borderType 边界类型
"""
kernel = np.ones((5, 5), np.float32) / 25
result = cv2.filter2D(img, ddepth=-1, kernel=kernel)

cv2.imshow('result', result)

"""
1. 方盒滤波 boxFilter(src, ddepth, ksize, anchor, normalize, borderType)
@:param ksize 卷积核大小
K = a * ones(?)
normalize = True, a = 1 / (W * H)  平均滤波 blur(src, ksize, anchor, borderType)
normalize = False, a = 1
"""
result2 = cv2.blur(img, ksize=(5, 5))
cv2.imshow('result2', result2)

"""
2. 高斯滤波
api -> GaussianBlur(img, ksize, sigmaX ,sigmaY, ...)
@:param sigmaX X的延展宽度
@:param sigmaY Y的延展宽度
"""
result3 = cv2.GaussianBlur(img, ksize=(5, 5), sigmaX=1.0)
cv2.imshow('result3', result3)

"""
3. 中值滤波
中值滤波对胡椒噪声效果明显
api -> medianBlur(img, ksize)
"""
result4 = cv2.medianBlur(img, ksize=5)
cv2.imshow('result4', result4)

"""
4. 双边滤波
可以保留边缘，同时可以对边缘的区域进行平滑处理
作用：进行美颜
api -> bilateralFilter(img, d, sigmaColor, sigmaSpace, ...)
@:param d 美化核的大小
@:param sigmaColor 颜色空间方差
@:param sigmaSpace 坐标空间方差
"""
result5 = cv2.bilateralFilter(img, d=7, sigmaColor=20, sigmaSpace=50)
cv2.imshow('result5', result5)

cv2.waitKey(0)
