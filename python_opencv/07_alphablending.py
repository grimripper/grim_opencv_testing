import cv2

def show_img_window(a,b):
    cv2.namedWindow(a, 0)
    cv2.imshow(a,b)

l = cv2.imread("lena.jpg", 1)
d = cv2.imread("lena-dunham.jpg", 1)

a = 0.75
b = 1-a

r = cv2.addWeighted(l, a, d, b, 0.0)

show_img_window("l", l)
show_img_window("d", d)
show_img_window("ld", r)

cv2.waitKey(0)
