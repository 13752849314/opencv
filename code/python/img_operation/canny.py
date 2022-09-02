# 边缘检测 Canny
"""
使用5*5高斯滤波消除噪声
计算图像梯度的方向（0°/45°/90°/135°）共四个方向
在四个方向上取局部最大值
取出最大值后进行阈值计算

api -> Canny(img, threshold1, threshold2, ...)
@:param threshold1 最小阈值
@:param threshold2 最大阈值
"""
import cv2

img = cv2.imread(r'../../../image/test.png')

dst = cv2.Canny(img, 50, 150)

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)
