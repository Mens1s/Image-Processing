import cv2
import os

"""
1-) create data set 
    negative, positive
2-) cascade dow
3-) cascade
4-) write algorithm
"""

# store pic
path = "images"

# pic size
imgWidth = 180
imgHeight = 120

# video Capture
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,180) # brigh

global countFolder

def saveDataFunc():
    global countFolder
    countFolder = 0

    while os.path.exists(path + str(countFolder)):
        countFolder += 1
    os.makedirs(path+str(countFolder))

saveDataFunc() 

count = 0
countSave = 0

while True:

    ret, img = cap.read()

    if ret:
        img = cv2.resize(img, (imgWidth, imgHeight))

        if count % 5 == 0:
            
            cv2.imwrite( path + str(countFolder)+ "/" + str(countSave)+ "_"+ ".png" , img)
            countSave += 1
        count += 1
        cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()