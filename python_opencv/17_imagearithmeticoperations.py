import cv2
import numpy as np

img1 = cv2.imread("lena.jpg")
img2 = cv2.imread("lena-dunham.jpg")

img = img1 + img2 # modulo operation
img = cv2.add(img1, img2) # saturating operation
img = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.namedWindow("img")
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

x = np.array([6], np.uint8)
y = np.array([251], np.uint8)

print cv2.add(x,y)
print x+y
