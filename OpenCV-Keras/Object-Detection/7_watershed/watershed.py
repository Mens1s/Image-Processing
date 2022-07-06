import cv2
import numpy as np
import matplotlib.pyplot as plt

coin = cv2.imread("coins.jpg")
plt.figure(), plt.imshow(coin), plt.axis("off")

# lpf: blurring
coin_blur = cv2.medianBlur(coin, 13)
plt.figure(), plt.imshow(coin_blur), plt.axis("off")

# grayscale
coin_gray = cv2.cvtColor(coin_blur, cv2.COLOR_BGR2GRAY)
plt.figure(), plt.imshow(coin_gray, cmap="gray"), plt.axis("off")

# binary threshold
ret, coin_trhresh = cv2.threshold(coin_gray, 75, 255, cv2.THRESH_BINARY )
plt.figure(), plt.imshow(coin_trhresh, cmap="gray"), plt.axis("off")

# counter
contours , hierarchy = cv2.findContours(coin_trhresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(coin,contours,i,(0,255,0),10)
plt.figure(), plt.imshow(coin), plt.axis("off")

coin = cv2.imread("coins.jpg")


# lpf: blurring
coin_blur = cv2.medianBlur(coin, 13)
plt.figure(), plt.imshow(coin_blur), plt.axis("off")

# grayscale
coin_gray = cv2.cvtColor(coin_blur, cv2.COLOR_BGR2GRAY)
plt.figure(), plt.imshow(coin_gray, cmap="gray"), plt.axis("off")

# binary threshold
ret, coin_trhresh = cv2.threshold(coin_gray, 65, 255, cv2.THRESH_BINARY )
plt.figure(), plt.imshow(coin_trhresh, cmap="gray"), plt.axis("off")

# acilma
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(coin_trhresh, cv2.MORPH_OPEN, kernel, iterations=2)
plt.figure(), plt.imshow(opening, cmap="gray"), plt.axis("off")

# distance between objects
dist_transforms = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

# small pic
ret, sure_for = cv2.threshold(dist_transforms, 0.4*np.max(dist_transforms),255,0)
plt.figure(), plt.imshow(sure_for, cmap="gray"), plt.axis("off")

# bigger pic
sur_back = cv2.dilate(opening, kernel, iterations=1)
sure_for = np.uint8(sure_for)

unknown = cv2.subtract(sur_back, sure_for)
plt.figure(), plt.imshow(unknown, cmap="gray"), plt.axis("off")

# connection
ret, marker = cv2.connectedComponents(sure_for)
marker += 1
marker[unknown == 255] = 0 
plt.figure(), plt.imshow(marker, cmap="gray"), plt.axis("off")

# havza
marker = cv2.watershed(coin, marker)
plt.figure(), plt.imshow(marker, cmap="gray"), plt.axis("off")

# counterz
contours , hierarchy = cv2.findContours(marker.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(coin,contours,i,(255,0,0),2)
plt.figure(), plt.imshow(coin), plt.axis("off")
