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
from sklearn.mixture import GaussianMixture as GMM


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
    threshold = 0.7 
    #empirically determined to be a good threshold
    s_thresh = [int(val > threshold) for val in norm_s_diff]
    #threshold the normalized signal. convert to int from boolean in order to 
    #perform logic of up or down transition
    s_thresh_up = signal_diff(s_thresh) > 0 
    #check for up transition (start of heart beat)
    BPM = np.sum(s_thresh_up)/((len(s_thresh_up)+1)/fs/60) 
    #count the number of heart beats and divide by the total time. Total time 
    #is calculated as the length of the measurement (samples) / fs (samples/s)
    #/ 60 (min/s). This gives us beats/min
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
    s_diff = np.append(s_diff, 0)
    #np.diff returns one shorter, so need to add a 0
    return s_diff

def detrend(s, n_avg):
    ma = np.zeros(s.size)
    for i in np.arange(0, len(s)):
        ma[i] = np.mean( s[i:(i + n_avg)] )    
    return s - ma

def normalize(s):
    s = s-np.min(s)
    s = s/np.max(s)
    return s

def remove_mean_offset(s):
    mean_s = np.mean(s)
    s = s - mean_s
    return s

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

    #print("Acessing File of ID: " + sub_id)
    i=0
    for sub_file in sub_files:
        #print("Accessing File: " + str(sub_file))
        
        data_array = np.genfromtxt(sub_file, delimiter = ',')
        heart_rate_data = data_array[:,4]
        t = data_array[:,0]

        heart_rate_data = detrend(heart_rate_data, 4)
        
        b,a = signal.butter(filter_order, filter_cutoff, btype='low')
        heart_rate_data = signal.lfilter(b,a,heart_rate_data)
        
        #shove things into list_data but not too much or it goes bonkers

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
    #print("sub_id: " +sub_id + " has " + str(i) + " Files recorded")
    total_files+=i

#print("Total Files Accessed: " + str(len(list_data)))
#print("Total sub_id: " + str(k))
#print("Total Files Opened: " + str(total_files))
i#f total_files==10*len(unique_ids):
 #   print("ALL FILES OPENED AND ACCESSED")
#else:
#    print("SOME FILES NOT ACCESSED")

#Actual ML stuff
#a = list_data.flatten()
#plt.plot(list_time, a)

#plt.hist(list_data)
#plt.show()

train_data = np.array([])
#make empty numpy array of size 0
hold_out_data = np.array([])
#make empty numpy array of size 0
train_ids = unique_ids
p=0
q=0
print("NUMBER OF TRAIN_IDS:" + str(len(train_ids)))
hold_out_subject = float(train_ids[9])


#print(type(sub_id))
#print(type(hold_out_subject))
#for now we’ll hold out the first training subject

for ind, sub_id in enumerate(list_sub):
    #enumerate the list_sub starting at 0. Look up enumerate function
    #print(hold_out_subject)
    if sub_id != hold_out_subject:
        p+=1
        #sub_id is not the same as hold_out_subject
        train_data = np.concatenate((train_data, list_data[ind]))
        #print(np.shape(train_data))
        #print(np.shape(list_data[ind]))
        #concatenate numpy array train_data with the list_data at ind
    else:
        q+=1
        hold_out_data = np.concatenate((hold_out_data, list_data[ind]))
        #concatenate numpy array hold_out_data with list_data at ind


start_index = 0
end_index = 100
gmm = GMM(n_components = 2).fit(train_data.reshape(-1,1))        
test_pred = gmm.predict(hold_out_data.reshape(-1,1))
plt.plot(test_pred[start_index:end_index])
hold_out_data = normalize(hold_out_data)
#hold_out_data = remove_mean_offset(hold_out_data)
plt.plot(hold_out_data[start_index:end_index])
plt.xlabel("Time")
plt.ylabel("Beat T or F")
#list_data = normalize(list_data)
#list_data = remove_mean_offset(list_data)

plt.show()














































    
