# part2
import cv2


def callback():
    pass


if __name__ == '__main__':
    cv2.namedWindow('color', cv2.WINDOW_NORMAL)

    img = cv2.imread('../../../image/test.png')

    print(img.shape)  # 高度，长度，通道数
    print(img.size)  # 高度 * 长度 * 通道数
    print(img.dtype)  # 数据类型 -> 位深

    colorspace = [cv2.COLOR_BGR2BGRA,
                  cv2.COLOR_BGR2RGBA,
                  cv2.COLOR_BGR2GRAY,
                  cv2.COLOR_BGR2HSV_FULL,
                  cv2.COLOR_BGR2YUV,
                  cv2.COLOR_BGR2HSV
                  ]
    cv2.createTrackbar('colorBar', 'color', 0, len(colorspace), callback)

    while True:
        bar = cv2.getTrackbarPos('colorBar', 'color')
        # 颜色空间转换
        cvt_img = cv2.cvtColor(img, colorspace[bar])
        cv2.imshow('color', cvt_img)

        key = cv2.waitKey(10)
        if key & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
