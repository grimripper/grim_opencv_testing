import cv2
import numpy as np

img = cv2.imread("sudoku.jpg")
print img.shape
rows,cols = img.shape[:2]

M = np.float32([
    [1,0,100],
    [0,1,50]
])

cv2.namedWindow('img')
dst = cv2.warpAffine(img, M, (cols,rows))
cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
