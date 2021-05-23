import cv2

img = cv2.imread("./Resources/lena.png")
print(img.shape)

width, height = 1000, 1000
imgResize = cv2.resize(img, (width, height))
print(imgResize.shape)

imgCropped = img[300:540, 0:512]
imgCropsize = cv2.resize(imgCropped, (img.shape[0], img.shape[1]))

cv2.imshow("lena", img)
cv2.imshow("lena Resized", imgResize)
cv2.imshow("lena Cropped", imgCropped)
cv2.imshow("lena Cropped", imgCropsize)

cv2.waitKey(0)
