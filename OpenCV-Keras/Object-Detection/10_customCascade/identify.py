import cv2

path = "cascade.xml"
objectName = "Pencil "
frameWidth = 200
frameHeight = 360
color = (255,0,0)

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

# trackbar
cv2.namedWindow("Result")
cv2.resizeWindow("Result", frameWidth, frameHeight + 100)
cv2.createTrackbar("Scale","Result",400,1000,empty)
cv2.createTrackbar("Neighbors","Result",4,50,empty)

cascade = cv2.CascadeClassifier(path)
while True:
    ret, img = cap.read()
    if ret:
        # convert bgr 2 gray
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #   detection parameters
        scaleVal = 1 + (cv2.getTrackbarPos("Scale","Result") / 1000)
        neighbour = cv2.getTrackbarPos("Neighbors", "Result")

        #   detection
        rects = cascade.detectMultiScale(gray, scaleVal, neighbour)

        for (x,y,w,h) in rects:
            cv2.rectangle( img , (x, y), (x+w,y+h), color,3)
            cv2.putText(img, objectName, (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
        
        cv2.imshow("Result", img)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break