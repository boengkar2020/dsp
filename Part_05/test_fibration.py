#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:19:45 2022

@author: sukarno
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy import signal


t, x = np.genfromtxt('mesin_mobil.csv',delimiter=',', unpack=True)

N = np.int32(np.prod(t.shape))#length of the array
Fs = 1/(t[1]-t[0]) 	#sample rate (Hz)
T = 1/Fs;
print("# Samples: ",N)
print ('# Sample time :',T)


#Plot data
plt.figure(1)  
plt.plot(t, x)
plt.xlabel('Time (seconds)')
plt.ylabel('Accel (g)')
plt.title('Mesin Mobil')
plt.grid()

#Compute RMS and Plot
w = np.int32(np.floor(Fs)); #width of the window for computing RMS
steps = np.int_(np.floor(N/w)); #Number of steps for RMS
t_RMS = np.zeros((steps,1)); #Create array for RMS time values
x_RMS = np.zeros((steps,1)); #Create array for RMS values
for i in range (0, steps):
	t_RMS[i] = np.mean(t[(i*w):((i+1)*w)]);
	x_RMS[i] = np.sqrt(np.mean(x[(i*w):((i+1)*w)]**2));  
plt.figure(2)  
plt.plot(t_RMS, x_RMS)
plt.xlabel('Time (seconds)')
plt.ylabel('RMS Accel (g)')
plt.title('RMS - Mesin Mobil')
plt.grid()

#Compute an plot FFT
plt.figure(3)  
xf = np.linspace(0.0, 1.0/(2.0*T), num = np.int32(N/2))
yf = fft(x)
plt.plot(xf, 2.0/N * np.abs(yf[0:np.int32(N/2)]))
plt.grid()
plt.xlabel('Frequency (Hz)')
plt.ylabel('Accel (g)')
plt.title('FFT - Mesin Mobil')

# Compute and Plot Spectrogram
plt.figure(4)  
f, t2, Sxx = signal.spectrogram(x, Fs, nperseg = np.int32(Fs/4))
plt.pcolormesh(t2, f, np.log(Sxx))
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.title('Spectrogram - Mesin Mobil')

