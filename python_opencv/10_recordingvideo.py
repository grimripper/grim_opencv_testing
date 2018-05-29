import cv2
import numpy as np

cv2.namedWindow("img", 1)

out = cv2.VideoWriter("output.avi", 0, 20.0, (640,480))
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret == True:
        #frame = cv2.flip(frame, 0)
        frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("img", frame2)
        out.write(frame)
        if cv2.waitKey(10) == 27:
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
