import cv2
from time import sleep

cv2.namedWindow("lena", 0)
img = cv2.imread("lena.bmp", cv2.CV_LOAD_IMAGE_COLOR)

cv2.imshow("lena", img)
cv2.waitKey(0)

t = cv2.getTickCount();
sleep(2)
t2 = cv2.getTickCount();
timepassed = (t2 - t)/cv2.getTickFrequency();
print("time passed = ")
print(timepassed)

cv2.waitKey(0)

