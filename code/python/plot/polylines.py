# part3 多边形

import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread(r'../../../image/test.png')

    # 多边形
    pts = np.array([(300, 10), (150, 100), (450, 100)], dtype=np.int32)
    cv2.polylines(img, [pts], isClosed=True, color=(0, 0, 255))

    # 填充
    cv2.fillPoly(img, [pts], (0, 255, 0))

    cv2.imshow('polyline', img)
    cv2.waitKey(0)
