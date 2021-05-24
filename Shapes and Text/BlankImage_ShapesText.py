# Importing libraries
import cv2
import numpy as np

# Creating an numpy array of zeros
img = np.zeros((512, 512, 3), np.uint8)

# Coloring the image, yellow
img[:] = 0, 255, 255

# Creating a line of green color
cv2.line(img, (0, 0), (512, 512), (0, 255, 0), 2)

# Creating a rectangle filled red color
cv2.rectangle(img, (350, 100), (450, 200), (0, 0, 255), cv2.FILLED)

# Creating a circle of blue color
cv2.circle(img, (150, 400), 50, (255, 0, 0), 3)

# Putting a text of green color
cv2.putText(img, "Draw Shapes ", (75, 50),
            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)

# Displaying the image
cv2.imshow("image", img)
cv2.waitKey(0)
