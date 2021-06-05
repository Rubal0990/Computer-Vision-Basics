# Importing Library
import cv2


# Function to detect click
def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


# Reading Image
img = cv2.imread('./../Resources/chess.jpg')

# Displaying Original Image
cv2.imshow("Original Image ", img)

# Function Call to detect click
cv2.setMouseCallback("Original Image ", mousePoints)
cv2.waitKey(0)
