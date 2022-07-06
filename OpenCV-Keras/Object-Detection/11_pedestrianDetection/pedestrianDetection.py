import cv2
import os

files = os.listdir()
img_list = []

for f in files:
    if f.endswith(".jpg"):
        img_list.append(f)

# hog tanimlayicisi

hog = cv2.HOGDescriptor()

hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

for image in img_list:

    img = cv2.imread(image)

    (rects, weights) = hog.detectMultiScale(img, padding=(8,8), scale=1.05)

    for(x,y,w,h) in rects:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255) ,2)
        

    cv2.imshow("Pedestrian", img)
    if cv2.waitKey(0) & 0xFF == ord("q"):
        continue