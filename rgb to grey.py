import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8); print(kernel)  # Separate the statements with a semicolon

path = "C:/Users/manoj/OneDrive/Pictures/Desktop/Documents/cv/image.jpg"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale", imgGray)
cv2.waitKey(0)