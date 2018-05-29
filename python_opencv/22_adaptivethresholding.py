import cv2
import numpy as np

img = cv2.imread('sudoku.jpg', 0)
#img = cv2.medianBlur(img, 5)
img = cv2.GaussianBlur(img, (5,5), 0)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
print ret
ret, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print ret
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th4 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

cv2.namedWindow('img')
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imshow('img', th1)
cv2.waitKey(0)
cv2.imshow('img', th2)
cv2.waitKey(0)
cv2.imshow('img', th3)
cv2.waitKey(0)
cv2.imshow('img', th4)
cv2.waitKey(0)
cv2.destroyAllWindows()
