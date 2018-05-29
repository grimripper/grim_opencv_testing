#NOT WORKING

import cv2
import numpy as np

cv2.namedWindow('res')
img1 = cv2.imread("lena.png")
img2 = cv2.imread("fresco.png")
rows,cols,shape = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('res', img2gray)
cv2.waitKey(0)
ret, mask = cv2.threshold(img2, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('res', mask)
cv2.waitKey(0)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('res', mask_inv)
cv2.waitKey(0)

#img1_bg = cv2.bitwise_and(img1, roi, roi, mask = mask_inv)
#
#img2_fg = cv2.bitwise_and(img2, img2, mask = mask)
#
# Put logo in ROI and modify the main image
#dst = cv2.add(img1_bg,img2_fg)
#img1[0:rows, 0:cols ] = dst

#cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
