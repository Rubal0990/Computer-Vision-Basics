# Import Libraries
import cv2
import numpy as np

# Creating an numpy array of zeros
circles = np.zeros((4, 2), np.int)
counter = 0

# Function to detect click and drawing a green circle
def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter = counter + 1
        print(circles)


# Reading Image
img = cv2.imread('Resources/chess.jpg')

while True:

    # Checking if all 4 Circles are drawn
    if counter == 4:
        # Parameters
        width, height = 250, 350

        # Creating the Bird-eye view of Image
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

        # Displaying the Bird-eye view of Original Image
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Output Image ", imgOutput)

    for x in range(0, 4):
        cv2.circle(img, (circles[x][0], circles[x][1]),
                   3, (0, 255, 0), cv2.FILLED)

    # Displaying Original Image
    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints)
    cv2.waitKey(1)
