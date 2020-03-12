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




directory = "/Users/mikeliu/Desktop/ECE 16/ece16-wi2020-m7liu/src/Python/LAB05/All_Heart_Beat_Data/*.csv"
allfiles = glob.glob(directory)
#unique = list(set([file.split("\\")[1][0:2] for file in set(allfiles)]))
single = list(set(file.split("\\")[0][86:88] for file in set(allfiles) ))
print(single)

failed_test = False
print("Numbers of Test")
for i in range(1, 13):
    test_condition = "{:02d}".format(i)
    
    test_result = test_condition in single
    print("Has " + str(test_condition) + "? " + str(test_result))
    if not(test_result):
        print("FAILED TEST " + str(i))
        failed_test = True
        break

# TEST 2: IS A LIST

if not(failed_test):
    print(failed_test)
    
    
    
    
    
for file in allfiles:
    #print(file)

    data_array = np.genfromtxt(file, delimiter=',')
    
#print(file.split("\\")[1][0:2] for file in set(allfiles) )
