import cv2
import numpy as np

# create  pic
img = np.zeros((512, 512, 3), np.uint8) # black img
print(img.shape)

cv2.imshow("Siyah", img)

# line
cv2.line(img, (0,0), (512,512), (0,255,0), 3 ) # pic, startPosition, endPosition, color, think(kalinlik)
cv2.imshow("Line", img)

# rectangle
cv2.rectangle(img, (0,0), (200,200), (255,0,0), cv2.FILLED)
cv2.imshow("Rectangle",img)

# circle
cv2.circle(img , (300,300), 45, (0,0,255))
cv2.imshow("Circle", img)

# text
cv2.putText(img, "Pic", (150,300), cv2.FONT_HERSHEY_COMPLEX, 2, (255,100,100))
cv2.imshow("TEXT", img)