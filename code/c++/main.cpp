//
// Created by 37157 on 2022/7/19.
//
#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>


using namespace cv;
using namespace std;

int main() {
    cout << 123 << endl;
    Mat image = imread(R"(D:\github\opencv\image\test.jpg)");
    namedWindow("hg", WINDOW_AUTOSIZE);
    imshow("hg", image);

    waitKey(0);
    cout << "end" << endl;
    return 0;
}
