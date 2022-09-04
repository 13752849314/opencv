# 轮廓查找

"""
为了检测的准确性，需要先对图像进行二值化或Canny操作
画轮廓时会修改输入的图像
"""
import cv2

img = cv2.imread(r'../../../image/lk.png', cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread(r'../../../image/lk.png')
cv2.imshow('img', img)
print(img.shape)

# 二值化
ret, binary = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', binary)
binary1 = binary.copy()

"""
api -> findContours(img, mode, method) -> (contours, hierarchy)
@:param mode 
enum {
    RETR_EXTERNAL  = 0, // 表示只检测外轮廓
    RETR_LIST      = 1, // 检测的轮廓不建立等级关系
    RETR_CCOMP     = 2, // 每层最多两级
    RETR_TREE      = 3, // 按树形存储轮廓
}
@:param method
enum {
    CHAIN_APPROX_NONE      = 1, // 保存所有轮廓上的点
    CHAIN_APPROX_SIMPLE    = 2, // 只保存角点
}
return:
@:param contours 轮廓
@:param hierarchy 层级
"""

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
print(hierarchy)

# 绘制轮廓
"""
api -> drawContours(img, contours, contourIdx, color, thickness=1, ...)
@:param contourIdx -1表示绘制所有轮廓
@:param thickness 线宽，-1是全部填充
"""
cv2.drawContours(img1, contours, contourIdx=1, color=(0, 0, 255), thickness=2)
cv2.imshow('contours', img1)

# 计算轮廓的面积和周长
# 1. 轮廓的面积
area0 = cv2.contourArea(contours[1])

# 2. 轮廓的周长
length0 = cv2.arcLength(contours[1], closed=True)  # closed 是否是闭合的轮廓

print('area=', area0, 'length=', length0)
cv2.waitKey(0)
