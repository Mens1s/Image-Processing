"""
Created on Thu Jun 22 21:35:05 2022

@author: mens1s
"""
import numpy as np

# it helps calculation of matrix

# 1 * 15 matrix
 
dizi = np.array(range(1,16))

print(dizi.shape)

dizi2 = dizi.reshape(3,5)

# burası en önemli yer 

print("Shape = ", dizi2.shape)
print("Boyut = ", dizi2.ndim)
print("Veri = ", dizi2.dtype.name)
print("Boy : ",dizi2.size)

# array type
print("Type : ", type(dizi2))

# Create 2D array

dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(dizi2D)

# all elements zeor
sifir_dizi = np.zeros((3,4))
print(sifir_dizi)

# all elemtns one
bir_dizi = np.ones((3,4))
print(bir_dizi)

# empty array
bos_dizi = np.empty((3,4))
print(bos_dizi)

# aralıkta n n artan dizi
dizi_aralik = np.arange(10,50,5)
print(dizi_aralik)

# n esit parca
dizi_bosluk = np.linspace(10,20,5)
print(dizi_bosluk)

# create float array
float_array = np.float32([[1,2],[3,4]])
print(float_array)

# math op
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a*b)

# functions
print(np.sum(a))
print(np.max(a))
print(np.min(a))
print(np.mean(a))
print(np.median(a))


# random get num
rastgele_ddizi = np.random.random((3,3))
print(rastgele_ddizi)

# index

dizi = np.array([1,2,3,4,5,6,7])
print(dizi[0])


# first 4 
print(dizi[:4])

# reversed
print(dizi[::-1])

#
dizi2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)

# dizinin 1. satir ve 1.sütün
print(dizi2D[0][0])
print(dizi2D[0,0])

# tüm satırlalrda bulunun 1 sütün
print(dizi2D[:,1])

# 1. satirdan 1-4 index arası
print(dizi2D[1,1:4])

# 1. satir tum sutunlar
print(dizi2D[-1,:])

# vector
dizi2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)

# get Vektor
vektor  = dizi2D.ravel()
print(vektor)

# get max index

print(vektor.argmax())