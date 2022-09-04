# swell 膨胀

import cv2
import numpy as np

img = cv2.imread(r'../../../image/test.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)

"""
api -> dilate(img, kernel, iterations=1)
"""

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
swell = cv2.dilate(img, kernel=kernel)

cv2.imshow('swell', swell)

cv2.waitKey(0)
