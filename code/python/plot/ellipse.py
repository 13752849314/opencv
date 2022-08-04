# part3 画椭圆
import cv2

if __name__ == '__main__':
    img = cv2.imread(r'../../../image/test.png')
    # 圆
    cv2.circle(img, (200, 200), 100, (0, 255, 0))
    # 椭圆
    cv2.ellipse(img, (200, 200), (100, 50), 0, 0, 360, (0, 0, 255))
    cv2.ellipse(img, (200, 200), (100, 50), 30, 0, 360, (0, 0, 255))
    cv2.ellipse(img, (200, 200), (100, 50), 60, 0, 360, (0, 0, 255))
    cv2.ellipse(img, (200, 200), (100, 50), 90, 0, 360, (0, 0, 255))
    cv2.ellipse(img, (200, 200), (100, 50), 120, 0, 360, (0, 0, 255))
    cv2.ellipse(img, (200, 200), (100, 50), 150, 0, 360, (0, 0, 255))
    cv2.ellipse(img, (200, 200), (100, 50), 180, 0, 360, (0, 0, 255))

    cv2.imshow('ellipse', img)
    cv2.imwrite(r'../../../image/ellipse.png', img)
    cv2.waitKey(0)
