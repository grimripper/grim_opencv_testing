import cv2
import numpy as np

#cv2.THRESH_BINARY
#cv2.THRESH_BINARY_INV
#cv2.THRESH_TRUNC
#cv2.THRESH_TOZERO
#cv2.THRESH_TOZERO_INV

img = cv2.imread("gradient.jpg")

ret,thresh1 = cv2.threshold(img, 127,255, cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img, 127,255, cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img, 127,255, cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img, 127,255, cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img, 127,255, cv2.THRESH_TOZERO_INV)

cv2.namedWindow('grad')

cv2.imshow('grad', img)
cv2.waitKey(0)
cv2.imshow('grad', thresh1)
cv2.waitKey(0)
cv2.imshow('grad', thresh2)
cv2.waitKey(0)
cv2.imshow('grad', thresh3)
cv2.waitKey(0)
cv2.imshow('grad', thresh4)
cv2.waitKey(0)
cv2.imshow('grad', thresh5)
cv2.waitKey(0)
cv2.destroyAllWindows()
