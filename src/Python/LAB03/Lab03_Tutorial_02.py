#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:12:26 2020

@author: mikeliu
"""

import serial

def setup_serial():
    serial_name = '/dev/cu.usbserial-14410'
    ser = serial.Serial(serial_name, 9600)  # open serial port
    print(ser.name)         # check which port was really used
    return ser

def send_serial(ser):
    S = 'Hello World\n'         
    ser.write(S.encode('utf-8'))         # write a string
    
def read_serial1(ser):
    s = ser.read(10).decode('utf-8')     # read 30 bytes and decode it
    print("s")

def readSerial2(ser):
    n=0
    while (n<30):
        s = ser.read(1).decode('utf-8')     # read 1 byte and decode it
        print(s)
        n=n+1

def readSerial3(ser):
    n=0
    full_string = []
    while (n<30):
        s = ser.read(1).decode('utf-8')     # read 1 byte and decode it
        full_string.append(s)
        n=n+1
    print(full_string)

def readSerial4(ser):
    while True:
        try:
            s = ser.read(1).decode('utf-8')         # read 1 byte and decode to utf-8
            print(s)
        except(KeyboardInterrupt):
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            break


def main():
    ser = setup_serial()
    #send_serial(ser)
    read_serial1(ser)
    #readSerial2(ser)
    #readSerial3(ser)
    #read_serial1(ser)
    #readSerial4(ser)
    ser.close()
    
    
if __name__== "__main__":
    main()


