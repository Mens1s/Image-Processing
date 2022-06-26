# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 17:26:38 2022

@author: ahmet
"""

import os

print(os.name)

curDir = os.getcwd()
print(curDir)

# new folder
f_name = "new_folder"
os.mkdir(f_name)

# f_rename
f_name = "new_folder2"
os.rename(f_name[:-1],f_name)

os.chdir(curDir+"\\"+f_name)
print(os.getcwd())

os.chdir(curDir)
print(os.getcwd())

files = os.listdir()
for f in files:
    if f.endswith(".py"):
        print(f)
        
os.rmdir(f_name)

for i in os.walk(curDir):
    print(i)
    
    
print(os.path.exists("les-01.py"))
