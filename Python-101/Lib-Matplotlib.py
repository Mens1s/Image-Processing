# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 17:06:22 2022

@author: mens1s
"""

# verileri gorsellestirme
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([4,3,2,1])

plt.figure()
plt.plot(x,y, color="red" , alpha = 0.7, label = "line")
plt.scatter(x,y,color ="blue", alpha = 0.4 , label = "scatter")
# color => renk , alpha => çizginin saydamligi 
# label => line adı bunu göstermek için plt.legen() yazmak gerekir
# plt.scatter() => boncuklar esit araliklarla
plt.title("Matplotlib")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
# ızgara yapısı

plt.xticks(range(6))

plt.legend()
plt.show()

#                        2 satir 1 sutun
fig, axes = plt.subplots(2,1, figsize=(9,7))
# iki resim arasindaki bosluk
fig.subplots_adjust(hspace = 0.5)

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,9,8,7,6,5,4,3,2,1]

axes[0].scatter(x,y)
axes[0].set_title("sub-1")
axes[0].set_ylabel("sub-1 y")
axes[0].set_xlabel("sub-1 x")

axes[1].scatter(y,x)
axes[1].set_title("sub-2")
axes[1].set_ylabel("sub-2 y")
axes[1].set_xlabel("sub-2 x")

# random resim
plt.figure()
img = np.random.random((50,50))
plt.imshow(img, cmap = "gray" ) # gray => 0.5 0 siyah 1 beyaz 
plt.axis("off")
plt.show()