# part1
import cv2
import numpy as np


def callback():
    pass


if __name__ == '__main__':
    cv2.namedWindow('TrackBar', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('TrackBar', 640, 360)

    cv2.createTrackbar('R', 'TrackBar', 0, 255, callback)
    cv2.createTrackbar('G', 'TrackBar', 0, 255, callback)
    cv2.createTrackbar('B', 'TrackBar', 0, 255, callback)

    img = np.zeros((360, 640, 3), dtype=np.uint8)
    while True:
        r = cv2.getTrackbarPos('R', 'TrackBar')
        g = cv2.getTrackbarPos('G', 'TrackBar')
        b = cv2.getTrackbarPos('B', 'TrackBar')

        img[:] = [b, g, r]
        cv2.imshow('TrackBar', img)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
