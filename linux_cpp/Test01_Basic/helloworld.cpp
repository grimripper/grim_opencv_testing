#include <iostream>
#include <opencv2/opencv.hpp>
using namespace std;
using namespace cv;

int main(int argc, char* argv[]) {
	cout << "Helloworld - OpenCV" << endl;

	Mat image = cv::imread("../../../images/lena.jpg");
	if (image.empty()) {
		cout << "Could not find image" << endl;
		return -1;
	}

	namedWindow("window");
	imshow("window", image);
	waitKey(0);
	destroyWindow("window");

	imwrite("out.png", image);

	return EXIT_SUCCESS;
}