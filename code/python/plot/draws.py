import cv2
import numpy as np

# l -> 线
# r -> 矩形
# c -> 圆
shape = 0
start_pos = (0, 0)
img = np.zeros((480, 640, 3), dtype=np.uint8)


def mouse_callback(event, x, y, flags, userdata):
    global shape, start_pos
    if event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN:
        start_pos = (x, y)
    elif event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP:
        if shape == 0:
            cv2.line(img, start_pos, (x, y), (0, 0, 255))
        elif shape == 1:
            cv2.rectangle(img, start_pos, (x, y), (0, 0, 255))
        elif shape == 2:
            a = x - start_pos[0]
            b = y - start_pos[1]
            r = int((a ** 2 + b ** 2) ** 0.5)
            cv2.circle(img, start_pos, r, (0, 0, 255))


# 创建窗口
cv2.namedWindow('draws', cv2.WINDOW_NORMAL)

# 设置鼠标回调
cv2.setMouseCallback('draws', mouse_callback)

while True:
    cv2.imshow('draws', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('l'):  # line
        shape = 0
    elif key == ord('r'):  # rectangle
        shape = 1
    elif key == ord('c'):  # circle
        shape = 2

cv2.destroyAllWindows()
