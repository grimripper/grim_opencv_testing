#include <iostream>
#include <opencv2/opencv.hpp>
using namespace std;
using namespace cv;

int main(int argc, char* argv[]) {
	cout << "Helloworld - OpenCV" << endl;

	if (argc != 2) {
		cout << "Usage: helloworld <image>" << endl;
		return -1;
	}

	Mat image = cv::imread(argv[1]);
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