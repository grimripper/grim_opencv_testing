#Scaling
import cv2
import numpy as np

cv2.namedWindow('img', 1)
cv2.namedWindow('res', 1)

img = cv2.imread("lena.jpg")
res = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

#height, width = img.shape[:2]
#res = cv2.resize(img, (width, 4*height), interpolation=cv2.INTER_CUBIC)

cv2.imshow('img', img)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
