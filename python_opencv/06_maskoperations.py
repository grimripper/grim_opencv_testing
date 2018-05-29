import cv2
import numpy

def show_img_window(a,b):
    cv2.namedWindow(a, 0)
    cv2.imshow(a,b)

kernel = numpy.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

img = cv2.imread("lena.jpg", 0)
show_img_window("orig", img)

# destination has same depth as orig
newimg = cv2.filter2D(img, -1, kernel)

show_img_window("new", newimg)

cv2.waitKey(0)
