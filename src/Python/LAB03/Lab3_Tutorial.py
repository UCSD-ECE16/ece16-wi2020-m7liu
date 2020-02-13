#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:16:11 2020

@author: mikeliu
"""

#Install Numpy
import numpy as np

#print (np.__version__)

#Numpy array
myPythonList = [1,9,8,3]
numpy_array_from_list = np.array(myPythonList)

a  = np.array([1,9,8,3])
#print(numpy_array_from_list + 10)
#print(a.shape)
#print(a.dtype)
c = np.array([(1,2,3),
              (4,5,6)])
#print(c.shape)
d = np.array([[[1, 2,3],[4, 5, 6]],
             [[7, 8,9],[10, 11, 12]]])
#print(d.shape)

test_array = np.array([0,10,4,12])
print(test_array.shape)
print(test_array-20)

test_2D_array = np.array([(0,10,4,12),(1,20,3,41)])
print(test_2D_array)

#Numpy zeroes and ones
print(np.zeros((2,2)))
print(np.zeros((10,20)))

#Numpy hstack() and vstack()
f = np.array([1,2,3])
g = np.array([4,5,6])

print('Horizontal Append:\n', np.hstack((f, g)))
print('Vertical Append:\n', np.vstack((f, g)))
test_hstack_array = np.hstack((test_array, test_array))
test_vstack_array = np.vstack((test_hstack_array,test_hstack_array,test_hstack_array,test_hstack_array))
print(test_vstack_array)

#Numpy arange
arrange_array1 = np.arange(-3,16,6)
print(arrange_array1)
arange_array2 = np.arange(-7,-20,-2)
print(arange_array2)

#Numpy linspace()
linspace_array = np.linspace(0,100,49)
print(linspace_array)

#setting values of an array
zero_array = np.zeros((3,4))
zero_array[0]=[12,3,12,2]
zero_array[1,0]=0
zero_array[:,1]=[3,0,2]
zero_array[2,:2]=[4,2]
zero_array[2,2:]=[3,1]
zero_array[:,2]=[1,1,3]
zero_array[1,3]=2
print(zero_array)

#Setting values of array from comma separated values
data_string = '1,2,3,4'
data_array = np.fromstring(data_string,dtype=int,sep=',')
print_array = data_array
for x in range(0,99):
    print_array=np.vstack((print_array,data_array),)
print(print_array)









