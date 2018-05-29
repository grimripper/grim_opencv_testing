import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')
cv2.namedWindow('controls')

# create trackbars for color change
cv2.createTrackbar('R','controls',0,255,nothing)
cv2.createTrackbar('G','controls',0,255,nothing)
cv2.createTrackbar('B','controls',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'controls',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','controls')
    g = cv2.getTrackbarPos('G','controls')
    b = cv2.getTrackbarPos('B','controls')
    s = cv2.getTrackbarPos(switch,'controls')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()
