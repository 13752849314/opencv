# part3 画线
import cv2

if __name__ == '__main__':
    img = cv2.imread(r'../../../image/test.png')
    # pt -> (x, y)
    # color -> (b, g, r)
    cv2.line(img, (10, 10), (100, 10), (0, 0, 255), thickness=2)
    cv2.line(img, (10, 10), (10, 100), (0, 0, 255), thickness=2)
    cv2.line(img, (10, 100), (100, 100), (0, 0, 255), thickness=2)
    cv2.line(img, (100, 10), (100, 100), (0, 0, 255), thickness=2)

    cv2.imshow('line', img)

    cv2.waitKey(0)
