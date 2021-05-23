import cv2

# Image
img = cv2.imread("./Resources/lena.png")
cv2.imshow("Lena", img)
cv2.waitKey(1000)

# Video
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    # img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Cam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
