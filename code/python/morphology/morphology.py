# 形态学
import cv2

img = cv2.imread(r'../../../image/test.png')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img', img)
cv2.imshow('img1', img1)

"""
1. 图像二值化
api -> threshold(img, thresh, maxval, type)
@:param img 最好为灰度图
@:param thresh 阈值
@:param maxval 超过阈值，替换为 maxval
@:param type enum {
    THRESH_BINARY     = 0, bit
    THRESH_BINARY_INV = 1, bit
    THRESH_TRUNC      = 2,
    THRESH_TOZERO     = 3,
    THRESH_TOZERO_INV = 4,
    THRESH_MASK       = 7,
    THRESH_OTSU       = 8,
    THRESH_TRIANGLE   = 16
}
"""

ret, result1 = cv2.threshold(img1, 180, 255, cv2.THRESH_BINARY)
print(ret)
cv2.imshow('result1', result1)

"""
2. 自适应阈值
api -> adaptiveThreshold(img, maxValue, adaptiveMethod, thresholdType, blockSize, C)
@:param adaptiveMethod 计算阈值的方法
enum {
    ADAPTIVE_THRESH_MEAN_C     = 0, // 计算邻近区域的平均值
    ADAPTIVE_THRESH_GAUSSIAN_C = 1 // 高斯窗口加权平均值
}
@:param blockSize 邻近区域的大小
@:param C 常量，应从计算出的平均值或加权平均值中减去
"""

result2 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
                                3, 0)
cv2.imshow('result2', result2)

cv2.waitKey(0)
