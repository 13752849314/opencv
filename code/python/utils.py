import cv2


def read_video(source):
    """
    读取视频数据
    :param source: 来源
    :return: 视频帧
    """
    cap = cv2.VideoCapture()
    if type(source) is int or type(source) is str:
        cap.open(source)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print("fps=", fps, "\nwidth=", width, "\nheight=", height)
    else:
        raise ValueError("Incorrect parameter input!")

    cv2.namedWindow(str(source), cv2.WINDOW_NORMAL)
    cv2.resizeWindow(str(source), width=width, height=height)

    frames = []  # save frames
    while cap.isOpened():
        success, image = cap.read()
        if success:
            frames.append(image)
            cv2.imshow(str(source), image)
            key = cv2.waitKey(fps)
            if key & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyWindow(str(source))
    print("读取完成：", len(frames))
    return frames, {
        'fps': fps,
        'width': width,
        'height': height,
        'resolution': (width, height)
    }


def save_video(filename, frames, fps, resolution, fourcc='mp4v'):
    """
    保存视频
    :param filename: 文件名
    :param frames: 视频帧
    :param fps: fps
    :param resolution: 分辨率
    :param fourcc:
    :return:
    """
    fcc = cv2.VideoWriter_fourcc(*fourcc)
    vw = cv2.VideoWriter(filename, fcc, fps, resolution)

    for frame in frames:
        vw.write(frame)
    vw.release()
    print("success!")
