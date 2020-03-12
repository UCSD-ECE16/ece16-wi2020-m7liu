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


directory = "/Users/mikeliu/Desktop/ECE 16/ece16-wi2020-m7liu/src/Python/LAB05/Heart_Beat_Data/*.csv"

allfiles = glob.glob(directory)
#print(allfiles)
i = 0
gridsize = (10,2)
fig = plt.figure(figsize=(10, 30))
ref = np.array([77,85,87,78,89,102,76,75,74,80]) #clip recorded heart rate
est_htime=np.array([])
est_hfreq=np.array([])

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
    heart_rate_time = calc_heart_rate_time(heart_filt, fs)
    est_htime = np.append(est_htime, heart_rate_time)
    print("Heart Rate Time: " + str(heart_rate_time))
    heart_rate_freq = calc_heart_rate_freq(heart_filt, fs)
    est_hfreq = np.append(est_hfreq, heart_rate_freq)
    print("Heart Rate Freq: " + str(heart_rate_freq))
    

    i+=1
    print("")
    
    
#est = est_htime
est = est_hfreq
[R,p] = pearsonr(ref,est)

plt.figure(1)
plt.clf()
plt.subplot(121)
plt.plot(ref,ref)
plt.scatter(ref,est)
plt.text(min(ref) + 2,max(est)+2,"R="+str(round(R,2)))
plt.ylabel("estimate HR (BPM)")
plt.xlabel("reference HR (BPM)")

avg = (ref + est) / 2 #take the average of gnd and est
dif = ref - est #take the difference of gnd and est
std = np.std(dif) #get the standard deviation of the difference (using np.std)
bias = np.mean(dif) #the mean value of the difference
upper_std = bias + 1.96 * std #the bias plus 1.96 times the std
lower_std = bias - 1.96 * std #the bias minus 1.96 times the std

print("TIME BIAS: " + str(bias))

plt.subplot(122)
plt.scatter(avg, dif)
plt.plot([np.min(avg),np.max(avg)],[bias,bias])
plt.plot([np.min(avg),np.max(avg)],[upper_std, upper_std])
plt.plot([np.min(avg),np.max(avg)],[lower_std, lower_std])
plt.text(np.max(avg)+5,bias,"mean="+str(round(np.mean(ref-est),2)))
plt.text(np.max(avg)+5,upper_std,"1.96STD="+str(round(upper_std,2)))
plt.text(np.max(avg)+5,lower_std,"-1.96STD="+str(round(lower_std,2)))
plt.ylabel("Difference of Est and Gnd (BPM)")
plt.xlabel("Average of Est and Gnd (BPM)")
plt.show()

    
    
    
    
    
    