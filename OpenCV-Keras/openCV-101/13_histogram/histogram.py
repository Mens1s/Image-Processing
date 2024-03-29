import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("red_blue.jpg")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img_vis), plt.title("org img")

img_hist = cv2.calcHist([img], channels= [0] , mask = None, histSize=[256], ranges = [0,256] )
plt.figure(), plt.plot(img_hist), plt.title("histogram img")


golden_gate = cv2.imread("goldenGate.jpg")
golden_gate_vis = cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(golden_gate), plt.title("golden gate img")

# MASK
mask = np.zeros(golden_gate.shape[:2], np.uint8)
plt.figure(), plt.imshow(mask, cmap="gray"), plt.title("mask-1 gate img")

mask[1500:2000, 1000:2000] = 255
plt.figure(), plt.imshow(mask, cmap="gray"), plt.title("mask-2 gate img")

masked_img_vis = cv2.bitwise_and(golden_gate_vis, golden_gate_vis, mask = mask)
plt.figure(), plt.imshow(masked_img_vis, cmap="gray"), plt.title("mask-2 gate img")

masked_img = cv2.bitwise_and(golden_gate, golden_gate, mask = mask)
masked_img_hist = cv2.calcHist([golden_gate], channels= [0] , mask = mask, histSize=[256], ranges = [0,256] )
plt.figure(), plt.plot(masked_img_hist), plt.title("gate histogram img")

# histogram esitleme
# karsılıklı artırma

img = cv2.imread("hist_equ.jpg",0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.title("hist img")

img_hist = cv2.calcHist([img], channels= [0] , mask = None, histSize=[256], ranges = [0,256])
plt.figure(), plt.plot(img_hist), plt.title("hist histogram img")

eq_hist = cv2.equalizeHist(img)
plt.figure(), plt.imshow(eq_hist, cmap="gray"), plt.title("hist histogram img")
