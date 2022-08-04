# part2
import cv2

if __name__ == '__main__':
    img = cv2.imread(r'../../../image/test.png', cv2.IMREAD_COLOR)

    b, g, r = cv2.split(img)
    b[10:100, 10:100] = 255
    g[10:100, 10:100] = 255

    img2 = cv2.merge((b, g, r))

    cv2.imshow('img', img)
    cv2.imshow('b', b)
    cv2.imshow('g', g)
    cv2.imshow('r', r)
    cv2.imshow('img2', img2)
    cv2.waitKey(0)
