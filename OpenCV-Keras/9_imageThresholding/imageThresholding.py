import cv2 
import matplotlib.pyplot as plt 

# remove other smaller details

img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")
plt.show()

# esikleme => Thresholding
# thres => 60 dan büyük olanlar not seem to us
_, threshImg = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY)

plt.figure()
plt.imshow(threshImg , cmap = "gray")
plt.axis("off")
plt.show()

_, thresh2Img = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY_INV)

plt.figure()
plt.imshow(thresh2Img , cmap = "gray")
plt.axis("off")
plt.show()

# details of threshold adative
                                            # algoritmalar                                      ortalama
thres_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
plt.figure()
plt.imshow(thres_img2, cmap="gray")
plt.axis("off")
plt.show()