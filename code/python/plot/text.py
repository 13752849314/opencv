import cv2

if __name__ == '__main__':
    img = cv2.imread(r'../../../image/test.png')
    cv2.putText(img, 'hello world!', (10, 400), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0))
    cv2.imshow('polyline', img)
    cv2.waitKey(0)
