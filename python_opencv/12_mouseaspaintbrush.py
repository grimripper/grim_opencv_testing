import cv2
import numpy as np


def draw_circle(event, x,y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print 'circle clicked at: ', x, y
        cv2.circle(img, (x,y), 50, (255,0,0), -1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("img", 0)
cv2.setMouseCallback("img", draw_circle)

while 1:
    #cv2.line(img, (0,0), (511,511), (255,255,255), 1)
    cv2.imshow("img", img)
    if cv2.waitKey(20) == 27:
        break

cv2.destroyAllWindows()

