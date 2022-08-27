import cv2


def fun1():
    """
    创建和显示窗口
    加载和保存图片
    :return:
    """
    cv2.namedWindow('hg', cv2.WINDOW_NORMAL)

    img = cv2.imread('../../image/test.jpg')

    cv2.imshow('hg', img)

    key = cv2.waitKey(0)

    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    elif key & 0xFF == ord('s'):
        cv2.imwrite('../../image/test.png', img)


def fun2():
    """
    视频采集从当前设备摄像头
    :return:
    """
    cv2.namedWindow('video', cv2.WINDOW_NORMAL)

    cap = cv2.VideoCapture(0)

    while True:
        success, image = cap.read()

        cv2.imshow('video', image)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def fun3():
    """
    视频采集从文件中读取
    :return:
    """
    cv2.namedWindow('video', cv2.WINDOW_NORMAL)

    cap = cv2.VideoCapture(r'D:\github\opencv\video\test.mp4')

    fps = cap.get(cv2.CAP_PROP_FPS)
    print("FPS=:", fps)

    while True:
        success, image = cap.read()
        if not success:
            break

        cv2.imshow('video', image)

        key = cv2.waitKey(int(1000 // fps))
        if key & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def fun4():
    from opencv.code.python.utils import read_video, save_video
    frames, parameters = read_video(r'D:\github\opencv\video\test.mp4')
    save_video(r'../../video/save.mp4',
               frames,
               fps=parameters.get('fps'),
               resolution=parameters.get('resolution'))
