# Importing library
import cv2

# Reading image
img = cv2.imread("./../Resources/lena.png")
# print(img.shape)

# Parameter for Image-sizing
width, height = 1000, 1000

# Resizing the image
imgResize = cv2.resize(img, (width, height))
# print(imgResize.shape)

# Cropping the image
imgCropped = img[300:540, 0:512]

# Resizing the image
imgCropsize = cv2.resize(imgCropped, (img.shape[0], img.shape[1]))

# Displaying the images
cv2.imshow("lena", img)
cv2.imshow("lena Resized", imgResize)
cv2.imshow("lena Cropped", imgCropped)
cv2.imshow("lena Cropped", imgCropsize)

cv2.waitKey(0)
