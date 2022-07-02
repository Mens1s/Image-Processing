import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("datai_team.jpg", 0)

plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off"), plt.title("original img"), plt.show()

# erozyon
kernel = np.ones((5,5), dtype=np.uint8)
result = cv2.erode(img, kernel, iterations=1)

plt.figure(), plt.imshow(result, cmap="gray"), plt.axis("off"), plt.title("erozyon img"), plt.show()

# genisleme dilation
result2 = cv2.dilate(img, kernel, iterations=1)
plt.figure(), plt.imshow(result2, cmap="gray"), plt.axis("off"), plt.title("dilate img"), plt.show()

# white noise
whiteNoise = np.random.randint(0,2,size = img.shape[:2])
whiteNoise = whiteNoise * 255
plt.figure(), plt.imshow(whiteNoise, cmap="gray"), plt.axis("off"), plt.title("white img"), plt.show()

noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap="gray"), plt.axis("off"), plt.title("white noise img"), plt.show()

# acilma
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap="gray"), plt.axis("off"), plt.title("white noise img"), plt.show()

# blackNoise
blackNoise = np.random.randint(0,2,size = img.shape[:2])
blackNoise = blackNoise * -255
plt.figure(), plt.imshow(blackNoise, cmap="gray"), plt.axis("off"), plt.title("black img"), plt.show()

blackNoise_img = blackNoise + img
blackNoise_img[blackNoise_img <= -245 ] = 0
plt.figure(), plt.imshow(blackNoise_img, cmap="gray"), plt.axis("off"), plt.title("black def img"), plt.show()

# kapatma close
closing = cv2.morphologyEx(blackNoise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(closing, cmap="gray"), plt.axis("off"), plt.title("black noise img"), plt.show()

# gradient

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap="gray"), plt.axis("off"), plt.title("black noise img"), plt.show()

