# 多边形逼近与凸包

import cv2


def draw_shape(src, points):
    for i in range(len(points)):
        if i == len(points) - 1:
            x, y = points[i][0]
            x1, y1 = points[0][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 2)
        else:
            x, y = points[i][0]
            x1, y1 = points[i + 1][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 2)


img = cv2.imread(r'../../../image/dbx.png')
cv2.imshow('img', img)

# 灰度图
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv2.threshold(grey, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', binary)

# 轮廓查找
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
img1 = img.copy()
cv2.drawContours(img1, contours, -1, (0, 0, 255), 2)

cv2.imshow('contours', img1)

"""
1. 多边形逼近
api -> approxPolyDP(curve, epsilon, closed)
@:param curve 轮廓
@:param epsilon 精度
@:param closed 是否是闭合轮廓
"""
e = 5
approx = cv2.approxPolyDP(contours[0], e, True)
draw_shape(img, approx)

cv2.imshow('approx', img)

"""
2. 凸包
api -> convexHull(points, clockwise=False, returnPoints=True)
@:param points 轮廓
@:param clockwise=True 顺时针
"""
hull = cv2.convexHull(contours[0])
draw_shape(img, hull)
cv2.imshow('hull', img)

cv2.waitKey(0)
