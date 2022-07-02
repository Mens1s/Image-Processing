from random import gauss
import cv2
import matplotlib.pyplot as plt
import warnings
import numpy as np
warnings.filterwarnings("ignore")

img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Original")
plt.show()

"""
Ortalama bulanıklastirma yöntemi
median blur
"""

dst2 = cv2.blur(img ,ksize = (3,3))

plt.figure()
plt.imshow(dst2)
plt.axis("off")
plt.title("dst2")
plt.show()

"""
gaussian blur kutu kutu ortalama
"""

gb = cv2.GaussianBlur(img, ksize=(3,3) , sigmaX=7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("gb")
plt.show()

"""
median blur
"""

md = cv2.medianBlur(img, ksize= 3)
plt.figure()
plt.imshow(md)
plt.axis("off")
plt.title("md")
plt.show()


def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var ** 0.5

    gauss = np.random.normal(mean, sigma, (row,col,ch) )
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy

# import image and normalize pic
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) / 255

plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Original-1")
plt.show()

gausianImage = gaussianNoise(img)

plt.figure()
plt.imshow(gausianImage)
plt.axis("off")
plt.title("Gauss Noisy")
plt.show()

gb = cv2.GaussianBlur(gausianImage, ksize = (3,3), sigmaX=7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("Gauss Noisy Blur")
plt.show()

def saltPaperNoise(image):

    row, col, ch = image.shape
    s_vs_p = 0.5

    amount = 0.004

    noisy = np.copy(image)


    # salt
    num_salt = int(np.ceil(amount * image.size * s_vs_p))
    coords = [np.random.randint(0,i-1,num_salt) for i in image.shape]
    noisy[coords] = 1

    # paper
    num_paper = int(np.ceil(amount * image.size * s_vs_p))
    coords = [np.random.randint(0,i-1,num_paper) for i in image.shape]
    noisy[coords] = 1

    return noisy

spImage = saltPaperNoise(img)
plt.figure()
plt.imshow(spImage)
plt.axis("off")
plt.title("Gauss Noisy Blur")
plt.show()

md = cv2.medianBlur(spImage.astype(np.float32), ksize= 3)
plt.figure()
plt.imshow(md)
plt.axis("off")
plt.title("md with noisy blur")
plt.show()
