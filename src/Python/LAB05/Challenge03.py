import glob
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from scipy import signal
from scipy import signal as sig
import os

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
    signal = self.detrend(signal)
    #filter the signal to remove high frequency noise
    signal = moving_average(signal, 8)

    signal = normalize_signal(signal)

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
        print(crossings)
        return ((crossings/2) * 60) / time_to_get_samples
    
    
def normalize_signal(s):
    norm_signal = (s - np.min(s))/(np.max(s)-np.min(s))
    return norm_signal


def moving_average(s,n_avg):
    ma = np.zeros(s.size)
    for i in np.arange(0,len(s)):
        ma[i] = np.mean(s[i:i+n_avg])
    return ma


directory = "/Users/mikeliu/Desktop/ECE 16/ece16-wi2020-m7liu/src/Python/LAB05/Heart_Beat_Data/*.csv"

allfiles = glob.glob(directory)
#print(allfiles)
i = 0
gridsize = (10,2)
fig = plt.figure(figsize=(10, 30))
ref = np.array([77,85,87,78,89,102,76,75,74,80]) #clip recorded heart rate

for file in allfiles:
    print(len(file))
    actualBPM = int(file[88:91])
    print("Clip recorded Heart: " + str(actualBPM))
    data_array = np.genfromtxt(file, delimiter=',')
    
    t = data_array[:,0]
    heart = data_array[:,4]
    
    #processing
    heart = signal.detrend(heart)
    b,a = signal.butter(3, 0.2, btype='low')
    heart_filt = signal.lfilter(b,a,heart)
    fs=50
    print("Calculated Heart Rate: " + str(calc_heart_rate_freq(heart_filt,fs)))
    heart_rate_time = calc_heart_rate_time(sig, heart, fs)
    print("Heart Rate Time: " + str(heart_rate_time))
    

    
    
    i+=1
    print("")