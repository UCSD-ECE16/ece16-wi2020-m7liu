# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math as mt
import math as cheese
from math import *
import numpy as np
a='Hello World!!!'
print(a)

b = ""
for x in range(0, 5):
    b=b+a[x]
    
print(b)

c = ""
for x in range(6, 11):
    c+=a[x]
    
print(c)

d = ""
for x in range(11, 14):
    d+=a[x]

print(d)

i = 0
j = 0
e = ""
f = "ello"
while i<len(a):
    if j<=len(f)-1 and a[i]==f[j]:
        e+=f[j]
        #print(e)
        j+=1
    if j>len(f):
        j=0
        e=""
    
    i+=1
if e=="ello":
    print("True")
print(e)
        
original_list = ['hi',1,2,'you']
new_list = original_list
newer_list = new_list[1:3]
newer_list[0:2] = ['how','are']
print(original_list)

print(mt.sqrt(4))
print(cheese.sqrt(4))
print(sqrt(4))

a = np.array([1,1])
b = np.array([1,1,1])
bigList=[]
bigList.append(a.tolist())
bigList.append(b.tolist())
print(bigList)
