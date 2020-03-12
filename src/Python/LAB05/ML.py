#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:43:40 2020

@author: mikeliu
"""
import glob
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from scipy import signal
from scipy import signal as sig
import os

def calc_heart_rate_freq(signal,fs):
   b,a = sig.butter(3, .2, btype='low')
   signal = sig.detrend(signal)
   signal = sig.lfilter(b,a,signal)
   Pxx, Freqs = plt.psd(signal, NFFT=len(signal), Fs=fs)
   slice_from = 3
   peaks, _ = sig.find_peaks(Pxx[slice_from:], distance=20)
   heart_freq = Freqs[slice_from:][peaks[0]]
   return heart_freq * 60



def calc_heart_rate_time(s,fs):
    s_diff = signal_diff(-s) #preprocess the signal, I chose to use diff
    norm_s_diff = normalize_signal(s_diff) #normalize the signal
    threshold = 0.7 #empirically determined to be a good threshold
    s_thresh = [int(val > threshold) for val in norm_s_diff] #threshold the normalized signal. convert to int from boolean in order to perform logic of up or down transition
    s_thresh_up = signal_diff(s_thresh) > 0 #check for up transition (start of heart beat)
    BPM = np.sum(s_thresh_up)/((len(s_thresh_up)+1)/fs/60) #count the number of heart beats and divide by the total time. Total time is calculated as the length of the measurement (samples) / fs (samples/s) / 60 (min/s). This gives us beats/min
    return BPM

def normalize_signal(s):
    norm_signal = (s - np.min(s))/(np.max(s)-np.min(s))
    return norm_signal


def moving_average(s,n_avg):
    ma = np.zeros(s.size)
    for i in np.arange(0,len(s)):
        ma[i] = np.mean(s[i:i+n_avg])
    return ma

def signal_diff(s):
    s_diff = np.diff(s,1,0)
    s_diff = np.append(s_diff, 0) #np.diff returns one shorter, so need to add a 0
    return s_diff

def detrend(s, n_avg):
    ma = np.zeros(s.size)
    for i in np.arange(0, len(s)):
        ma[i] = np.mean( s[i:(i + n_avg)] )    
    return s - ma


file_directory = "/Users/mikeliu/Desktop/ECE 16/ece16-wi2020-m7liu/src/Python/LAB05/All_Heart_Beat_Data/*.csv"
directory = "/Users/mikeliu/Desktop/ECE 16/ece16-wi2020-m7liu/src/Python/LAB05/All_Heart_Beat_Data"
allfiles = glob.glob(file_directory)
#unique = list(set([file.split("\\")[1][0:2] for file in set(allfiles)]))
unique_ids = list(set(file.split("\\")[0][86:88] for file in set(allfiles) ))
#print(directory)
#print(unique_ids)

list_data = np.array([])
list_sub = np.array([])
list_ref = np.array([])
list_time = np.array([])
#sub_id in the list of unique_ids

j=0
k=0
total_files=0
for sub_id in unique_ids:
    #using glob get the files of all files with this subject id
    sub_files = glob.glob(directory + "//" + sub_id + "_*_*.csv")
    k+=1
    #print(sub_files)
    filter_order = 3
    filter_cutoff = 0.2
    #print(i)
    print("Acessing File of ID: " + sub_id)
    i=0
    for sub_file in sub_files:
        print("Accessing File: " + str(sub_file))
        
        data_array = np.genfromtxt(sub_file, delimiter = ',')
        heart_rate_data = data_array[:,4]
        t = data_array[:,0]
        #print(np.arange(0, len(heart_rate_data)))
        #print(len(heart_rate_data))
        heart_rate_data = detrend(heart_rate_data, 4)
        
        b,a = signal.butter(filter_order, filter_cutoff, btype='low')
        heart_rate_data = signal.lfilter(b,a,heart_rate_data)
        
        #shove things into list_data but not too much or it goes bonkers
        #if list_data[j].size > 500:
            #list_data[j]=list_data[j]
        if list_data.size > 0:
            list_data = np.vstack((list_data, heart_rate_data[:500]))
        else:
            list_data = heart_rate_data[:500]
        list_sub = np.append(list_sub, int(sub_id))
        heartrate_ref_string = sub_file.split("_")
        heartrate_ref = int(heartrate_ref_string[len(heartrate_ref_string) - 1].split(".")[0])

        list_ref = np.append(list_ref, heartrate_ref)
        for l in range (0, 500): 
            j+=2000
            list_time=np.append(list_time,j)
        i+=1
    print("sub_id: " +sub_id + " has " + str(i) + " Files recorded")
    total_files+=i
        #each file in the list of files for this subject
        #data = #read the csv
        #hr_data = #get the ppg signal from data using slicing
        #preprocess your hr_data:removing baseline, smooth your signal using a low pass filter and normalize. 
        #append the preprocessed data to list_data
        #append the subject id to list_sub
        #retrieve the reference heart rate from the filename.
        #append the reference heart rate to list_ref
print("Total Files Accessed: " + str(len(list_data)))
print("Total sub_id: " + str(k))
print("Total Files Opened: " + str(total_files))
if total_files==10*len(unique_ids):
    print("ALL FILES OPENED AND ACCESSED")
else:
    print("SOME FILES NOT ACCESSED")
a = list_data.flatten()
plt.plot(list_time, a)



    
#print(file.split("\\")[1][0:2] for file in set(allfiles) )
