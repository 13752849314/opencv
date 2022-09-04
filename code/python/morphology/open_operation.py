# open operation 开运算
import cv2
import numpy as np

img = cv2.imread(r'../../../image/h.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)

"""
开运算 = 腐蚀 + 膨胀  去除大图形外的小图形
闭运算 = 膨胀 + 腐蚀  去除大图形内的小图形
形态学梯度 = 膨胀 - 腐蚀  求图形的边缘
顶帽运算 = 原图 - 开运算  得到大图形外的小图形
黑帽运算 = 原图 - 闭运算  得到大图形内的小图形
api -> morphologyEx(img, op, kernel)
@:param op 操作类型
enum {
    MORPH_ERODE    = 0, // 腐蚀
    MORPH_DILATE   = 1, // 膨胀
    MORPH_OPEN     = 2, // 开运算
    MORPH_CLOSE    = 3, // 闭运算
    MORPH_GRADIENT = 4, // 形态学梯度
    MORPH_TOPHAT   = 5, // 顶帽运算
    MORPH_BLACKHAT = 6  // 黑帽运算
}
"""

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
op = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel=kernel)
cv2.imshow('op', op)

cl = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel=kernel)
cv2.imshow('cl', cl)

grad = cv2.morphologyEx(cl, cv2.MORPH_GRADIENT, kernel=kernel)
cv2.imshow('grad', grad)

th = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel=kernel)
cv2.imshow('th', th)

bh = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel=kernel)
cv2.imshow('bh', bh)

cv2.waitKey()
