import cv2
import matplotlib.pyplot as plt
import numpy as np

# template matching : sablon esleme
# ana resimde kucuk resim arama
img = cv2.imread("cat.jpg", 0)
temp = cv2.imread("cat_face.jpg", 0)

h, w = temp.shape

methods = ["cv2.TM_CCOEFF", "cv2.TM_CCOEFF_NORMED"," cv2.TM_CCORR", 
            "cv2.TM_CCOEFF_NORMED" ,"cv2.TM_SQDIFF", "cv2.TM_SQDIFF_NORMED"]

for meth in methods:
    method = eval(meth)

    res = cv2.matchTemplate(img, temp, method)
    print(res.shape)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    top_left = 0
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0]+ w, top_left[1] + h)

    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    plt.figure()
    plt.subplot(121), plt.imshow(res, cmap = "gray")
    plt.title("Matched"), plt.axis("off")

    plt.subplot(122), plt.imshow(img, cmap = "gray")
    plt.title("Math result"), plt.axis("off")
    plt.suptitle(meth)

    plt.show()
