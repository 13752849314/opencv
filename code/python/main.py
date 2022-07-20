import cv2

if __name__ == '__main__':
    a = cv2.imread(r'..\..\image\test.jpg')
    print(123)
    cv2.imshow("hg", a)
    cv2.waitKey(0)
