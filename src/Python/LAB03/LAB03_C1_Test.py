#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:26:10 2020

@author: mikeliu
"""
import numpy as np

incoming_stream = b'1',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'2',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'3',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'4',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'5',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'6',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'7',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'8',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'9',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'1',b'0',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n'

string_buffer = []
data_array = np.array([])
a=0

for incoming_byte in incoming_stream:
    c = incoming_byte.decode('utf-8') #this takes the place of reading the byte from serial
    if(c=='\n'): # c is '\n'
        str = ""
        data_string = str.join(string_buffer) #JOIN buffer 
        print(data_string)

        temp_data_array = np.array(data_string)#csv string to 1x4 np array
        if(False):#data_array.size==0): #data_array is empty
            data_array = temp_data_array
            
        else:

            data_array = np.vstack((data_array,temp_data_array)) #vstack temp_data_array to end of data_array

        # reset buffer to []
        string_buffer = []
    else:
       # append the new char to string_buffer
        string_buffer.append(c)
#data_array=np.vstack(([1],[2]))
print(data_array)
