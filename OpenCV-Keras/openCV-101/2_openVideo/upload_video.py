# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 18:14:36 2022

@author: ahmet
"""

import cv2
import time

# video name
video_name = "MOT17-04-DPM.mp4"

# upload video
cap = cv2.VideoCapture(video_name)

print("Genislik : ", cap.get(3))
print("Yukseklik : ", cap.get(4))

if not cap.isOpened():
    print("HATA")
    
# return => true or false
# frame => every picture in video

ret = True
while ret:
    ret, frame = cap.read()
    
    if ret == True:
        time.sleep(0.01)
        cv2.imshow("Video", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()