# 图像运算
## 图像加减乘除
```python
import cv2
import numpy as np

img = cv2.imread(r'../../../image/test.png')

# print(img.shape)

img1 = np.ones((800, 1280, 3), np.uint8) * 50

cv2.imshow('orig', img)
result = cv2.add(img, img1)  # +
result1 = cv2.subtract(img, img1)  # -
result2 = cv2.multiply(img, img1)  # *
result3 = cv2.divide(img, img1)  # /

cv2.imshow('add_result', result)
cv2.imshow('sub_result', result1)
cv2.imshow('mut_result', result2)
cv2.imshow('div_result', result3)
cv2.waitKey(0)

```
## 图像的溶合
```python
# 图像的溶合
import cv2
import numpy as np

"""
api -> addWeighted(A, alpha, B, beta, gamma)
alpha, beta 为权重
gamma 静态权重
"""

img = cv2.imread(r'../../../image/test.png')
# print(img.shape)
back = np.zeros(img.shape, np.uint8)

result = cv2.addWeighted(img, 0.7, back, 0.3, 0)
cv2.imshow('add2', result)
cv2.waitKey(0)

```
## 图像的位运算
```python
# 图像的位运算
import cv2
import numpy as np

"""
1. 非运算
api -> bitwise_not(img)
"""

img = cv2.imread(r'../../../image/test.png')

result1 = cv2.bitwise_not(img)

cv2.imshow('result1', result1)

"""
2. 与运算
api -> bitwise_and(img1, img2)
"""
img2 = np.zeros(img.shape, np.uint8)
img2[50:500, 50:500] = 255
cv2.imshow('img2', img2)
result2 = cv2.bitwise_and(img, img2)
cv2.imshow('result2', result2)

"""
3. 或运算与异或运算
api -> bitwise_or(img1, img2)
api -> bitwise_xor(img1, img2)
"""
result3 = cv2.bitwise_or(img, img2)
result4 = cv2.bitwise_or(img, img2)
cv2.imshow('result3', result3)
cv2.imshow('result4', result4)
cv2.waitKey(0)

```
7-1