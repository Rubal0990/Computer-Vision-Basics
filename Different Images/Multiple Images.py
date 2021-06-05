import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)
print(kernel)

img = cv2.imread("Resources/lena.png")

# Direct-GrayScale
imgDGS = cv2.imread("lena.jpg", 0)

# Function-GrayScale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur-Image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 8)

# Canny-Image(Edges)
imgCanny = cv2.Canny(imgBlur, 100, 100)

# Dilation
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

# Eroded
imgEroded = cv2.dilate(imgDilation, kernel, iterations=2)

# Displaying Images
cv2.imshow("lena", img)
cv2.imshow("imgDGS", imgDGS)
cv2.imshow("imgGray", imgGray)
cv2.imshow("imgBlur", imgBlur)
cv2.imshow("imgCanny", imgCanny)
cv2.imshow("imgDilation", imgDilation)
cv2.imshow("imgEroded", imgEroded)
cv2.waitKey(0)
