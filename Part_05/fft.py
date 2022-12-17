#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:45:10 2022

@author: sukarno
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft

t, x = np.genfromtxt('mesin_mobil.csv',delimiter=',', unpack=True)

#Plot data
plt.figure(1)  
plt.plot(t, x)
plt.xlabel('Time (seconds)')
plt.ylabel('Accel (g)')
plt.title('Mesin Mobil')
plt.grid()


N = np.int32(np.prod(t.shape))#length of the array
Fs = 1/(t[1]-t[0]) 	#sample rate (Hz)
T = 1/Fs;
print("# Samples: ",N)
print ('# Sample time :',T)


#Compute an plot FFT
plt.figure(2)  
xf = np.linspace(0.0, 1.0/(2.0*T), num = np.int32(N/2))
yf = fft(x)
plt.plot(xf, 2.0/N * np.abs(yf[0:np.int32(N/2)]))
plt.grid()
plt.xlabel('Frequency (Hz)')
plt.ylabel('Accel (g)')
plt.title('FFT - Mesin Mobil')