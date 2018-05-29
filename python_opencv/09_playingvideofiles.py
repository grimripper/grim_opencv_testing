import numpy as np
import cv2

cv2.namedWindow("img", 0)
cap = cv2.VideoCapture("quetzal.avi")
while cap.isOpened():
    ret, frame = cap.read()
    if ret == False:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("img", gray)
    if cv2.waitKey(33) == 27:
        break

cap.release()
cv2.destroyAllWindows()
