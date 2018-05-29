import cv2;
img = cv2.imread(r"C:\Skydrive\2013-10-11 Jyotsana's 2nd baby shower\IMG_0144.JPG", cv2.CV_LOAD_IMAGE_COLOR);
cv2.namedWindow("camera", 1);
cv2.imshow("camera", img);
cv2.waitKey(0);
cv2.destroyWindow("camera");
