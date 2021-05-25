# Importing libraries
import cv2
import numpy as np

# Reading image
img1 = cv2.imread('./Resources/lena.png', 0)
img2 = cv2.imread('./Resources/lena.png')
print(img1.shape)
print(img2.shape)

# Resizing the image
img1 = cv2.resize(img1, (0, 0), None, 0.5, 0.5)
img2 = cv2.resize(img2, (0, 0), None, 0.5, 0.5)

# Converting image from BGR-Image to GrayScale-Image
img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)

# Stacking the images
hor = np.hstack((img1, img2))  # Horizontal
ver = np.vstack((img1, img2))  # Vertical

# Displaying the images
cv2.imshow('Vertical', ver)
cv2.imshow('Horizontal', hor)
cv2.waitKey(0)
