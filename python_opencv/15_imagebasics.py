import cv2
import numpy as np

img = cv2.imread("lena.jpg")
#b,g,r = cv2.split(img)
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
zero = np.zeros((img.shape[0], img.shape[1], 1), np.uint8)
cv2.namedWindow("img")

cv2.imshow("img", img)
cv2.waitKey(0)

blue_image = cv2.merge((b, zero, zero))
cv2.imshow("img", blue_image)
cv2.waitKey(0)

green_image = cv2.merge((zero, g,zero))
cv2.imshow("img", green_image)
cv2.waitKey(0)

red_image = cv2.merge((zero,zero,r))
cv2.imshow("img", red_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
