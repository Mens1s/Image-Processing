import cv2 
import numpy as np

# get image black and white
img = cv2.imread("odev2.jpg", 2)
img1 = img.copy()
# show image
cv2.imshow("Originial Image", img)

# detect corner and show it
edges = cv2.Canny(image = img, threshold1 = 200, threshold2 = 255)
cv2.imshow("Corner Detected Image", edges)

# get haarcascade
fCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# do face recegnotion
face_rect = fCascade.detectMultiScale(img, minNeighbors = 7)
for (x,y,w,h) in face_rect:
    cv2.rectangle(img1,(x,y),(x+w,y+h),(255,255,255),6)
cv2.imshow("FACE", img1)

# get HOG algorithm
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# get result with using hog algorithm and img
(rects, weights) = hog.detectMultiScale(img, padding = (8, 8), scale = 1.05)

for (xA,yA,xB,yB) in rects:
    cv2.rectangle(img,(xA,yA),(xB,yB), (0,0,255) , 2)

cv2.imshow("FACE detection with HOG", img)