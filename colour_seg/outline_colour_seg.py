import cv2
import cvzone
import numpy as np
from cvzone.ColorModule import ColorFinder

cap = cv2.VideoCapture(0)  # Use camera number 0
cap.set(3, 640)
cap.set(4, 480)

myColorFinder = ColorFinder(False)

def empty(a):
    pass

# Trackbars for HSV adjustment
cv2.namedWindow("Settings")
cv2.resizeWindow("Settings", 640, 240)
cv2.createTrackbar("Hue Min", "Settings", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Settings", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Settings", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Settings", 255, 255, empty)
cv2.createTrackbar("Val Min", "Settings", 155, 255, empty)
cv2.createTrackbar("Val Max", "Settings", 255, 255, empty)

def outlineDetection(img, mask):
    # Find contours in the mask (mask is already single-channel)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw the contours on the original image
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)  # Green color for contours
    
    return img

while True:
    success, img = cap.read()
    
    # Get HSV values from trackbars
    h_min = cv2.getTrackbarPos("Hue Min", "Settings")
    h_max = cv2.getTrackbarPos("Hue Max", "Settings")
    s_min = cv2.getTrackbarPos("Sat Min", "Settings")
    s_max = cv2.getTrackbarPos("Sat Max", "Settings")
    v_min = cv2.getTrackbarPos("Val Min", "Settings")
    v_max = cv2.getTrackbarPos("Val Max", "Settings")

    hsvVals = {'hmin': h_min, 'smin': s_min, 'vmin': v_min, 'hmax': h_max, 'smax': s_max, 'vmax': v_max}

    imgColor, mask = myColorFinder.update(img, hsvVals)

    # Apply outline detection
    imgOutlined = outlineDetection(img.copy(), mask)

    # Display the results
    cv2.imshow("Original", img)
    cv2.imshow("Color Detection", imgColor)
    cv2.imshow("Outlined Image", imgOutlined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
