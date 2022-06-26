import cv2
import numpy as np

img = cv2.imread("kart.png")
cv2.imshow("Original", img)

width = 400
height = 500

# corner of pictures
pts1 = np.float32([[203,0],[0,476],[541,150],[338,617]])

# transformed corners which I want
pts2 = np.float32([[0, 0],[0, height],[width, 0],[width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Last Pic", imgOutput)