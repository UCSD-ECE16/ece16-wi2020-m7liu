#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:01:54 2020

@author: mikeliu
"""


import glob
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from scipy import signal
from scipy import signal as sig

from HR import HR 

hr = HR()

def calc_heart_rate_freq(signal,fs):
   b,a = sig.butter(3, .2, btype='low')
   signal = sig.detrend(signal)
   signal = sig.lfilter(b,a,signal)
   Pxx, Freqs = plt.psd(signal, NFFT=len(signal), Fs=fs)
   slice_from = 3
   peaks, _ = sig.find_peaks(Pxx[slice_from:], distance=20)
   heart_freq = Freqs[slice_from:][peaks[0]]
   return heart_freq * 60

def calc_heart_rate_time(self, signal, fs):
    # invert source
    signal = -signal
        
    #filter the signal to remove baseline drifting
    signal = self.detrend(signal, 16)
    #filter the signal to remove high frequency noise
    signal = self.moving_average(signal, 8)

    signal = self.normalize_signal(signal)

    threshold = 0.5
    goingUp = signal[0] < threshold
    crossings = 0

#Count the number of times the signal crosses a threshold.
    for i in range(signal.size):
        current_sample = signal[i]
    
        if goingUp and current_sample > threshold:
            goingUp = False
            crossings = crossings + 1
        else:
            if not goingUp and current_sample < threshold:
                goingUp = True
                crossings = crossings + 1
        
        # Calculate the beats per minute.
        time_to_get_samples = (1/fs) * signal.size
        return ((crossings/2) * 60) / time_to_get_samples
    
    
directory = "/Users/mikeliu/Desktop/ECE 16/ece16-wi2020-m7liu/src/Python/LAB05/Heart_Beat_Data/*.csv"
allfiles = glob.glob(directory)
#print(allfiles)
i = 0
gridsize = (10,2)
fig = plt.figure(figsize=(10, 30))
for file in allfiles:
    print(file)
    data_array = np.genfromtxt(file, delimiter=',')
    t = data_array[:,0]
    heart = data_array[:,4]
    heart = signal.detrend(heart)
    b,a = signal.butter(3, 0.2, btype='low')
    heart_filt = signal.lfilter(b,a,heart)
    
    plt.subplot2grid(gridsize, (i,0)) #plot time and heart rate
    plt.xlabel("Time")
    plt.ylabel("PPG Reading")
    plt.plot(t, heart_filt)
    fs=50
    plt.subplot2grid(gridsize,(i,1))
    #print(calc_heart_rate_freq(heart,fs))
    Pxx, Freqs = plt.psd(heart, NFFT=len(t), Fs=fs)
    highest_freq = Freqs[np.argmax(Pxx)]
    i+=1
    
    
    