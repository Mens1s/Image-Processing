import cv2
import matplotlib.pyplot as plt

einstein = cv2.imread("einstein.jpg", 0)
plt.figure(), plt.imshow(einstein, cmap="gray"), plt.axis("off")

# classification
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_rect = face_cascade.detectMultiScale(einstein)

for (x,y,w,h) in face_rect:
    cv2.rectangle(einstein, (x,y), (x+w,y+h), (255,255,255), 10 )
plt.figure(), plt.imshow(einstein, cmap="gray"), plt.axis("off")

barca = cv2.imread("barcelona.jpg", 0)
plt.figure(), plt.imshow(einstein, cmap="gray"), plt.axis("off")

face_rect = face_cascade.detectMultiScale(barca, minNeighbors = 7)

for (x,y,w,h) in face_rect:
    cv2.rectangle(barca, (x,y), (x+w,y+h), (255,255,255), 10 )
plt.figure(), plt.imshow(barca, cmap="gray"), plt.axis("off")

# onLive

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        face_rect = face_cascade.detectMultiScale(frame, minNeighbors = 7)

        for (x,y,w,h) in face_rect:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255), 10 )
        cv2.imshow("Face Detected", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()
