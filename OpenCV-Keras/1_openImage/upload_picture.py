import cv2

# image read
img = cv2.imread("picture\\messi5.jpg",0)

# to do pic
cv2.imshow("First Pic", img)

k = cv2.waitKey(0) &0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("picture\\messi_gray.png",img)
    cv2.destroyAllWindows()