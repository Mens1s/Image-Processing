# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 16:45:15 2022

@author: mens1s
"""

import pandas as pd

dictionary = { "isim" : ["ali","veli","kenan","murat","ayse","hilal"],
              "yas" : [15,16,17,33,45,56],
              "maas" : [100,150,240,350,110,220] }

veri = pd.DataFrame(dictionary)

print(veri)

# first 5 line
print(veri.head)

# only columns
print(veri.columns)

# veri info
print(veri.info())

# statics
print(veri.describe())

# yas sutunu
print(veri["yas"])

# add info
veri["sehir"] = ["ank","ist","kon","izmir","burs","antalya"]
print(veri)

# yas sutunu
print(veri.loc[:,"yas"])

# yas sutunu ve 3 satir
print(veri.loc[:2,"yas"])

# yas ve sehir arasi sutunu ve 3 satir
print(veri.loc[:2,"yas":"sehir"])

# yas ve sehir  sutunu ve 3 satir
print(veri.loc[:2,["yas","isim"]])

# tersten
print(veri.loc[::-1,:])

# yas sutunu with iloc
print(veri.iloc[:,1])

# ilk 3 satir ve yas isim
print(veri.iloc[:2,[1,0]])

# filters

dictionary = { "isim" : ["ali","veli","kenan","murat","ayse","hilal"],
              "yas" : [15,16,17,33,45,66],
              "sehir" : ["izmir","ankara","konya","ankara","ankara","antalya"] }

veri = pd.DataFrame(dictionary)

# yas > 22

filtre1 = veri.yas > 22
fVeri = veri[filtre1]
print(fVeri)

# ort yas
ortYas = veri.yas.mean()

veri["YAS_GRUBU"] = ["kucuk" if ortYas > i else "buyuk" for i in veri.yas]
print(veri)

# birlestirme merge 

sozluk1 = {
        "isim" : ["ali","veli","kenan"],
        "yas" : [15,16,17],
        "sehir" : ["izmir","ankara","konya"]
        }
veri1 = pd.DataFrame(sozluk1)

sozluk2 = {
        "isim" : ["murat","ayse","hilal"],
        "yas" : [33,45,66],
        "sehir" : ["ankara","ankara","antalya"]
        }
veri2 = pd.DataFrame(sozluk2)

# dikey
veri_dikey = pd.concat([veri1,veri2], axis=0)
print(veri_dikey)

# yatay
veri_yatay = pd.concat([veri1,veri2], axis=1)
print(veri_yatay)
