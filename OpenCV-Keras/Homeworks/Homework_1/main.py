import matplotlib.pyplot as plt
import cv2

# 1-) get picture black-white
img = cv2.imread("odev1.jpg",0)

# 2-) Draw Pic
cv2.imshow("Originial Image", img)

# 3-) Get image size
print("Image shape : ", img.shape)

# 4-) Resize image 4/5
resized = cv2.resize(img, (int(img.shape[1] * 4 / 5),int (img.shape[0] * 4 / 5)))
cv2.imshow("Resized Image", resized)

# 5-) Add "dog" text to pic
textIMG = img 
cv2.putText(textIMG,"DOG",(400,196), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,0),4)
cv2.imshow("textedIMG", textIMG)

# 6-) Threshold 50< to white
_, threshedIMG = cv2.threshold(img, thresh=50, maxval=255, type=cv2.THRESH_BINARY)
cv2.imshow("Threshed IMG ", threshedIMG)

# 7-) Gaussian Blur
gausedIMG = cv2.GaussianBlur(img, (3, 3), sigmaX= 7) 
cv2.imshow("Gaused IMG", gausedIMG)

# 8-) Laplacian Gradyan
laplacianIMG = cv2.Laplacian(img, ddepth=cv2.CV_64F)
cv2.imshow("Laplacian IMG", laplacianIMG)

# 9-) Histogram of Originial IMG
histogramIMG = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.figure()
plt.plot(histogramIMG)
plt.title("Histogram IMG")
