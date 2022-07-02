import cv2

# get image 
img = cv2.imread("lenna.png")
print("Original image shape : ", img.shape)
cv2.imshow("originial", img)

# resize
imgResized = cv2.resize(img, (800,800))
print("Resized Img Shape : ", imgResized.shape)
cv2.imshow("Resized image", imgResized)

# crop
imgCropped = img[:400,:100]  # y, x
cv2.imshow("Cropped img", imgCropped)