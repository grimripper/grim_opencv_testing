import cv2
import time
import numpy as np

#cv2.setUseOptimized(False)
print cv2.useOptimized()

img1 = cv2.imread("fresco.png")
e1 = cv2.getTickCount()
t1 = time.time()
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1, i)
e2 = cv2.getTickCount()
t2 = time.time()
t = (e2 - e1)/cv2.getTickFrequency()
print t
print t2-t1

x = np.uint8([5])
t1 = cv2.getTickCount()
for i in range(0,1000):
    y = np.square(x)
t2 = cv2.getTickCount()
print (t2 - t1)/1001
