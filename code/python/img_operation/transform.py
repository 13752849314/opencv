# 图像变换
import cv2
import numpy as np

img = cv2.imread(r'../../../image/test.png')
size = img.shape

"""
1. 图像的缩放
api -> resize(src, dsize, dst, fx, fy, interpolation)
@:param dsize: 目标尺寸
@:param fx: x轴的缩放因子
@:param fy: y轴的缩放因子
@:param interpolation: 插值算法
INTER_NEAREST(临近插值，速度快，效果差)
INTER_LINEAR(双线性插值，原图中的4个点)
INTER_CUBIC(三次插值，16个点)
INTER_AREA(效果最好)
"""

result1 = cv2.resize(img, (size[1] // 2, size[0] // 2), interpolation=cv2.INTER_AREA)

cv2.imshow('img', img)
cv2.imshow('result1', result1)

"""
2. 图像翻转
api -> flip(img, flipCode)
@:param flipCode
==0 上下
> 0 左右
< 0 上下+左右
"""
result2 = cv2.flip(img, -1)
cv2.imshow('result2', result2)

"""
3. 图像旋转
api -> rotate(img, rotateCode)
@:param rotateCode
ROTATE_90_CLOCKWISE
ROTATE_180
ROTATE_90_COUNTERCLOCKWISE 270
"""
result3 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('result3', result3)

"""
4. 仿射变换
api -> warpAffine(src, M, dsize, flags, mode, value)
@:param M 变换矩阵
@:param dsize 输出尺寸
@:param flags 与resize中的插值算法一致
@:param mode 边界外推法标志
@:param value 填充边界的值
"""

# 平移矩阵
#                       右           下
M = np.float32([[1, 0, 100], [0, 1, 100]])
result4 = cv2.warpAffine(img, M, (size[1], size[0]))
cv2.imshow('result4', result4)

# 变换矩阵
"""
api -> getRotationMatrix2D(center, angle, scale)
@:param center 中心点
@:param angle 角度 逆时针
@:param scale 缩放比例
"""
M1 = cv2.getRotationMatrix2D((size[1] / 2, size[0] / 2), 15, 0.3)
result5 = cv2.warpAffine(img, M1, (size[1], size[0]))
cv2.imshow('result5', result5)

src = np.float32([[400, 300], [800, 300], [400, 1000]])
dst = np.float32([[200, 400], [600, 500], [150, 1100]])
M2 = cv2.getAffineTransform(src, dst)
result6 = cv2.warpAffine(img, M2, (size[1], size[0]))
cv2.imshow('result6', result6)

cv2.waitKey(0)
