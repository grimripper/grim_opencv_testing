import cv2

cv2.namedWindow("camera", 1)
cv2.namedWindow("camera_gray", 1)

webCamHndlr = cv2.VideoCapture(0)

print 'width = '
print webCamHndlr.get(3)
print 'height = '
print webCamHndlr.get(4)
print 'FPS = '
print webCamHndlr.get(5)
print 'Brightness = '
print webCamHndlr.get(10)
print 'Contrast = '
print webCamHndlr.get(11)
print 'Saturation = '
print webCamHndlr.get(12)
print 'Hue = '
print webCamHndlr.get(13)
print 'Gain = '
print webCamHndlr.get(14)
print 'Exposure = '
print webCamHndlr.get(15)

while True:
    ret,img = webCamHndlr.read()
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("camera", img)
    #cv2.imshow("camera_gray", gray)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
