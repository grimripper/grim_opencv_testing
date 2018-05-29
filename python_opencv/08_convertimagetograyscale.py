import cv2
import numpy as np

img = cv2.imread("lena.jpg", 0)
cv2.namedWindow("img", 0)
cv2.imshow("img", img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("lena_gray.png", img)
    cv2.destroyAllWindows()
