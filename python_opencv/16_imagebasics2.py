import cv2
import numpy as np

img = cv2.imread("lena.jpg")

cv2.namedWindow("img")
cv2.imshow("img", img)
cv2.waitKey(0)

replicated_image = cv2.copyMakeBorder(img, 10,10,10,10, cv2.BORDER_REPLICATE)
cv2.imshow("img", replicated_image)
cv2.waitKey(0)

reflect_image = cv2.copyMakeBorder(img, 10,10,10,10, cv2.BORDER_REFLECT)
cv2.imshow("img", reflect_image)
cv2.waitKey(0)

reflected101_image = cv2.copyMakeBorder(img, 10,10,10,10, cv2.BORDER_REFLECT_101)
cv2.imshow("img", reflected101_image)
cv2.waitKey(0)

wrap_image = cv2.copyMakeBorder(img, 10,10,10,10, cv2.BORDER_WRAP)
cv2.imshow("img", wrap_image)
cv2.waitKey(0)

constant_image = cv2.copyMakeBorder(img, 10,10,10,10, cv2.BORDER_CONSTANT)
cv2.imshow("img", constant_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
