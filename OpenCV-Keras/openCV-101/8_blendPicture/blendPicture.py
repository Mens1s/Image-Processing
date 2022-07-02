import cv2
from cv2 import imshow
import matplotlib.pyplot as plt

img1 = cv2.imread("img1.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("img2.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# shapes must be equal
img1 = cv2.resize(img1, (600,600))
img2 = cv2.resize(img2, (600,600))

# blend pictures = alpha*img1 + beta*img2

blended = cv2.addWeighted(src1=img1,alpha=0.5,src2=img2,beta=0.5, gamma=0)
# cv2.imshow("blendedPic",blended)
plt.figure()
plt.imshow(blended)