#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:59:58 2020

@author: mikeliu
"""
import numpy as np
import serial

#Make the variables below global
string_buffer = []
num_buffer = []
num_array= np.array([])
data_array = np.array([])
graph_array = np.array([])
sample_number=0

def setup_serial():
    serial_name = '/dev/cu.usbserial-14140'
    ser = serial.Serial(serial_name, 9600)  # open serial port
    print(ser.name)         # check which port was really used
    return ser


def receive_data(ser):
    # Send start data
    start = "Start Data\n"
    stop = "Stop Data\n"
    ser.write(start.encode('utf-8'))
    
    while sample_number<100:
        try:
            receive_sample(ser)
        except(KeyboardInterrupt):
            # Send stop data 
            ser.write(stop.encode('utf-8'))
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            break
    # Send stop data
    #np.diff(data_array)

    ser.write(stop.encode('utf-8'))
    ser.close()
    #np.diff(data_array, n=1, axis=0)
    

    return data_array
        
def receive_sample(ser):
    global string_buffer
    global num_buffer
    global data_array
    global num_array
    global sample_number
    # read a byte from serial (remember to decode)
    s = ser.read(1).decode('utf-8')
    if(s!=',' and s!='\n'):
        num_buffer.append(s)
    if(s==',' or s=='\n'):
        num_string=''.join(num_buffer)
        temp_num_array=np.array(int(num_string))
        if(num_array.size==0):
            num_array=temp_num_array
        else:
            num_array=np.hstack((num_array,temp_num_array))
 
        num_buffer=[]
    
    if(s=='\n'):# received \n
        sample_number+=1
        #data_string = ''.join(string_buffer) #JOIN buffer 
        #print(data_string)
        #temp_data_array = np.array(data_string) #string to np array
        #print(num_array)
        if(data_array.size==0): #data_array is empty 
            #data_array = temp_data_array
            data_array=num_array
        else:
            #data_array = np.vstack((data_array,temp_data_array)) #vstack temp_data_array to end of data_array
            data_array = np.vstack((data_array,num_array))
        # reset string_buffer to []
        #string_buffer=[]
        
        num_array=np.array([]);
    else:
        # append the new char to string_buffer
        string_buffer.append(s)
        


def calc_sampling_rate(data_array):
    #code to calculate sampling rate from data_array
    x = np.array([[1, 3, 6, 10], [0, 5, 6, 8]])
    a=np.diff(data_array,n=1,axis=0)
    print(a)
    print(np.mean(a,axis=0))
    #print(data_array.shape)
    #print(data_array)
    print("done")

    
def main():
    ser = setup_serial()
    graph_array=receive_data(ser)
    calc_sampling_rate(graph_array)
    ser.close()
    
    
if __name__== "__main__":
    main()
