import cv2
import numpy as np

#img1 = np.zeros((512,512,3), np.uint8)
#img1[:,:,0] = 255
#cv2.namedWindow("img")
#cv2.imshow("img", img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

green = np.uint8([[[0,255,0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print hsv_green

img1 = cv2.imread("lena.jpg")
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

cap = cv2.VideoCapture(0)
#
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    #Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5)
    if k == 27:
        break
cv2.destroyAllWindows()

