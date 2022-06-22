# lists

lists = [1,2,3,4,5]
print(type(lists))

tList = [0,"a","asd","12",1.5]
print(type(tList))
print(type(tList[len(tList) - 1]))

# tuple
# unchanged

tuples = (1,2,3,4,5,2,1,1,6,"a")
print(type(tuples))
print(tuples[5])
print(tuples.count(1))

tuple_xyz = (1,2,3)
x, y, z = tuple_xyz

print(x,y,z)

# deque
# listenin boyutunu tanımlanır ve circular olur

from collections import deque
dq = deque(maxlen = 3)

dq.append(2)
dq.append(3)
dq.append(4)
dq.append(5)

print(dq) # 3 4 5 , 2 gider

dq.appendleft(6)

print(dq) # 6 3 4 , 5 gider

# dictionary

# key => value

dicts = {
    "ist" : 34,
    "ank" : 6,
    "kon" : 42    
        }
print(dicts["ist"])

print(dicts.keys()) # ist ank kon

print(dicts.values()) #34 6 12

# lambda func

fc = lambda x , y, z  : x *y* z

print(fc(2,3,6))

# yield 
"""

-iterasyon
-generator
-yield

"""

#iterasyon yineleme
liste1 = [1,2,3]

for i in liste1:
    print(i)
    
# generetor yineleyeciler
# generator değerleri bellekte saklamaz yeri gelince anında uretirler
# memory friendly

generator = (x for x in range(1,4))

for i in generator:
    print(i)

# yield 
# funct eğer return olarak generator döndürürse
# yield kullanılır

def createGenerator():
    liste = range(1,4)
    for i in liste:
        yield i

generator = createGenerator()

for i in generator:
    print(i)
