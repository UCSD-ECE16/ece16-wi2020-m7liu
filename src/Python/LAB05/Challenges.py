#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:32:03 2020

@author: mikeliu
"""



from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


data_array = np.genfromtxt('appendix_a.csv', delimiter=',')#get data from Appendix A and save as .csv.

fs = 50#sampling rate in Hz
t = data_array[:,0]#get the time array
x = data_array[:,1]#get the x-acceleration array
y = data_array[:,2]
z = data_array[:,3]
heart = data_array[:,4]
det = signal.detrend(heart)

filter_order = 3
filter_cutoff = 0.0032
b,a = signal.butter(filter_order, filter_cutoff, btype='high')

x_filt = signal.lfilter(b,a,heart)
w, h = signal.freqz(b,a)
print(x_filt)
#
gridsize = (3,2)
fig = plt.figure(figsize=(12, 8))
ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=1)
plt.plot(w, 20 * np.log10(abs(h)))
ax2 = plt.subplot2grid(gridsize, (1, 0))
plt.plot(t,x)
ax3 = plt.subplot2grid(gridsize, (1, 1))
plt.psd(x, NFFT=len(t), Fs=fs) #plot the power spectral density
ax4 = plt.subplot2grid(gridsize, (2, 0))
plt.plot(t,x_filt)
ax5 = plt.subplot2grid(gridsize, (2, 1))
plt.psd(x_filt, NFFT=len(t), Fs=fs) #plot the power spectral density


