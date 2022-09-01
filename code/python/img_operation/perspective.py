# 透视变换

import cv2
import numpy as np

src1 = []
index = 0


def mouse_callback(event, x, y, flags, userdata):
    global index
    if event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN:
        src1.append([x, y])
        index += 1
        print('index=', index, (x, y))


"""
api -> warpPerspective(img, M, dsize, ...)
M -> getPerspectiveTransform(src, dst)
"""

img = cv2.imread(r'../../../image/perspective.jpg')
cv2.namedWindow('per')
cv2.setMouseCallback('per', mouse_callback)
while True:
    cv2.imshow('per', img)
    key = cv2.waitKey(5) & 0xFF
    if key == ord('q') or index == 4:
        cv2.destroyWindow('per')
        break
print(src1)
src = np.float32(src1)
dst = np.float32([[0, 0], [400, 0], [0, 400], [400, 400]])
M = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(img, M, (400, 400))
cv2.imshow('img', img)
cv2.imshow('result', result)

cv2.waitKey(0)
