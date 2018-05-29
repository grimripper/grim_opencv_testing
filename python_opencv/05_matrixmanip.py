import cv2;

# Stored in BGR (n rows, m columns)
# Stored in Grayscale (n rows, m columns)

img = cv2.imread("lena.bmp", cv2.CV_LOAD_IMAGE_COLOR);

print(img[0][1])
