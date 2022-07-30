//
// Created by 37157 on 2022/7/26.
//
#include "part1.h"

/**
 * 创建和显示窗口
 * 加载和保存图片
 */
void fun1() {
    Mat image = imread(R"(D:\github\opencv\image\test.jpg)"); // 加载图片

    namedWindow("hg", WINDOW_NORMAL); // 新建窗口

    imshow("hg", image); // 展示图片

    int key = waitKey(0);

    if (key == (int) ('q')) {
        cout << key << endl;
        destroyAllWindows();
    } else if (key == (int) ('s')) {
        cout << key << endl;
        bool b = imwrite(R"(D:\github\opencv\image\test.png)", image);
        cout << b << endl;
    }
}

/**
 * 视频采集从当前设备摄像头
 */
void fun2() {
    namedWindow("video", WINDOW_NORMAL);

    // 获取视频设备
    VideoCapture cap = VideoCapture(0);
    Mat image;
    while (true) {

        bool success = cap.read(image); // cap >> image

        imshow("video", image);

        int key = waitKey(1);

        if (key == (int) ('q')) {
            cout << key << endl;
            break;
        }
    }

    cap.release();
    destroyAllWindows();
}

/**
 * 视频采集从文件中读取
 * error: 无法读取视频文件 -- ffmpeg
 */
void fun3() {
    namedWindow("video1", WINDOW_AUTOSIZE);

    VideoCapture cap;
    cap.open(R"(D:\github\opencv\video\test.mp4)");
    cout << cap.isOpened() << endl;

    double fps = cap.get(CAP_PROP_FPS);
    cout << "fps=" << fps << endl;
    Mat image;

    while (true) {
        cap >> image;
        if (image.empty()) {
            break;
        }
        imshow("video1", image);
        int key = waitKey(41);
        if (key == (int) ('q')) {
            break;
        }
    }

    cap.release();
    destroyAllWindows();
}
