#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:15:27 2020

@author: edwardwang
"""

import serial
import numpy as np
from Libraries.Data import Data
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
class Connection:

    def __init__(self, serial_name, baud_rate):
        self.serial_name = serial_name
        self.baud_rate = baud_rate
        self.data = Data()
        self.setup_connection()
        self.string_buffer = []

        
    def setup_connection(self):
        self.ser = serial.Serial(self.serial_name, self.baud_rate)  # open serial port
    
    def close_connection(self):
        self.ser.close()
        
    def send_serial(self, message):
        self.ser.write(message.encode('utf-8'))         # write a string

    def read_serial(self):
        while True:
            try:
                s = self.ser.read(1).decode('utf-8')        # read 1 byte
                print(s)
            except(KeyboardInterrupt):
                self.close_connection()
                print("Exiting program due to KeyboardInterrupt")
                break

        
    def start_streaming(self):
        self.send_serial('start data\n')
    
    def receive_data(self):
        c = self.ser.read(1).decode('utf-8')         # read 1 byte
        if( c == '\n'):
            data_string = ''.join(self.string_buffer)
            temp_data_array = np.fromstring(data_string,dtype=int,sep=',')
            self.data.add_data(temp_data_array)
            self.string_buffer = []
            
        else:
           self.string_buffer.append(c)
    
    def end_streaming(self):
        self.send_serial('stop data\n')