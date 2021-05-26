# Importing Libraries
import cv2
import numpy as np

# Reading Image
img = cv2.imread('Resources/chess.jpg')

# Parameters
width, height = 250, 350

# Points for Wrap Prespective
pts1 = np.float32([[204, 200], [278, 169], [266, 238], [342, 203]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Creating the Bird-eye view of Image
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# Drawing Circles on Original Image
for x in range(0, 4):
    cv2.circle(img, (pts1[x][0], pts1[x][1]), 15, (0, 255, 0), cv2.FILLED)

# Displaying the Original Image
cv2.imshow("Original Image", img)

# Displaying the Bird-eye view of Original Image
cv2.imshow("Output Image", imgOutput)
cv2.waitKey(0)
