# corrosion 腐蚀

import cv2
import numpy as np

img = cv2.imread(r'../../../image/test.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)

"""
api -> erode(img, kernel, iterations=1)
@:param iterations=1 腐蚀的次数
"""

kernel = np.ones((5, 5), dtype=np.uint8)
erode = cv2.erode(img, kernel=kernel, iterations=1)

cv2.imshow('erode', erode)

"""
获取卷积核
api -> getStructuringElement(shape, ksize)
@:param shape 卷积核类型
enum {
    MORPH_RECT    = 0, // 全1
    MORPH_CROSS   = 1, // 交叉
    MORPH_ELLIPSE = 2  // 椭圆
}
"""

kernel1 = cv2.getStructuringElement(cv2.MORPH_CROSS, ksize=(5, 5))
print(kernel1)

erode1 = cv2.erode(img, kernel=kernel1, iterations=1)

cv2.imshow('erode1', erode1)

cv2.waitKey(0)
