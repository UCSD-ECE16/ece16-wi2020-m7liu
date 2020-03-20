#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:21:58 2020

@author: edwardwang
"""
import matplotlib.pyplot as plt

class Visualize:
    def plotData(data_array):
        plt.clf()
        plt.subplot(411)
        
        plt.title("Example Data Plot")
        
        plt.plot(data_array[:,0],data_array[:,1])
        
        plt.ylabel("X Amplitude")
        
        plt.subplot(412)
        plt.plot(data_array[:,0],data_array[:,2])
        plt.ylabel("Y Amplitude")
        
        plt.subplot(413)
        plt.plot(data_array[:,0],data_array[:,3])
        plt.ylabel("Z Amplitude")
        
        plt.subplot(414)
        plt.plot(data_array[:,0],-data_array[:,4])
        
        plt.xlabel(u'Time(${\mu}s$)')
        plt.ylabel("R Amplitude")
        
        plt.show()
        
    def plotAccel(data_array):
        plt.clf()
        plt.subplot(311)
        
        plt.title("Example Data Plot")
        
        plt.plot(data_array[:,0],data_array[:,1])
        
        plt.ylabel("X Amplitude")
        
        plt.subplot(312)
        plt.plot(data_array[:,0],data_array[:,2])
        plt.ylabel("Y Amplitude")
        
        plt.subplot(313)
        plt.plot(data_array[:,0],data_array[:,3])
        plt.ylabel("Z Amplitude")
    
        
        plt.xlabel(u'Time(${\mu}s$)')
        
        plt.show()