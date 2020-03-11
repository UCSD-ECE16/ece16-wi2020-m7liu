#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 12:25:26 2020

@author: mikeliu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math

data_array = np.genfromtxt('appendix_a.csv', delimiter=',')#get data from Appendix A and save as .csv.

fs = 50#sampling rate in Hz
t = data_array[:,0]#get the time array
x = data_array[:,1]#get the x-acceleration array
y = data_array[:,2]
z = data_array[:,3]
heart = data_array[:,4]
det = signal.detrend(heart)

plt.subplot(411)
plt.plot(t, z)
plt.subplot(412)
plt.psd(z, NFFT=len(t), Fs=fs) #plot the power spectral density
plt.subplot(413)
plt.psd(det, NFFT=len(t), Fs=fs)
Pxx, Freqs = plt.psd(det, NFFT=len(t), Fs=fs)
plt.subplot(414)
plt.plot(Freqs, Pxx)
#print(Pxx)
#print("\n")
#print(Pxx[20:])
skipped_index=0
index_skipped=skipped_index+1
pmax = np.argmax(Pxx[skipped_index:])+index_skipped
print(pmax)
plt.show()

