#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 11:46:37 2020

@author: mikeliu
"""


import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

gnd = np.array([1, 2, 3, 4])
est = np.array([5, 1, 6,2])

[R,p] = pearsonr(gnd,est)

plt.figure(1)
plt.clf()
plt.subplot(121)
plt.plot(gnd,gnd)
plt.scatter(gnd,est)
plt.text(np.amin(gnd) + 2,np.amax(est)+2,"R="+str(round(R,2)))
plt.ylabel("estimate HR (BPM)")
plt.xlabel("reference HR (BPM)")

avg = (gnd+est)/2.0 #take the average of gnd and est
dif = (gnd-est) #take the difference of gnd and est
std = np.std(dif) #get the standard deviation of the difference (using np.std)
bias = np.mean(dif) #the mean value of the difference
upper_std = bias+(1.96*std)#the bias plus 1.96 times the std
lower_std = bias-(1.96*std)#the bias minus 1.96 times the std

plt.subplot(122)
plt.scatter(avg, dif)
plt.plot([np.min(avg),np.max(avg)],[bias,bias])
plt.plot([np.min(avg),np.max(avg)],[upper_std, upper_std])
plt.plot([np.min(avg),np.max(avg)],[lower_std, lower_std])
plt.text(np.max(avg)+5,bias,"mean="+str(round(np.mean(gnd-est),2)))
plt.text(np.max(avg)+5,upper_std,"1.96STD="+str(round(upper_std,2)))
plt.text(np.max(avg)+5,lower_std,"-1.96STD="+str(round(lower_std,2)))
plt.ylabel("Difference of Est and Gnd (BPM)")
plt.xlabel("Average of Est and Gnd (BPM)")
plt.show()
