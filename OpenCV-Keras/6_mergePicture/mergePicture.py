import cv2
import numpy as np
# get image
img = cv2.imread("lenna.png")
cv2.imshow("original", img)

hor = np.hstack((img, img))
cv2.imshow("Horizontall Merge",hor)

ver = np.vstack((img,img))
cv2.imshow("Vertical Image", ver)