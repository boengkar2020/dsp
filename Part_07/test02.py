#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 06:11:03 2022

@author: sukarno
"""

import numpy as np
import scipy.fft as fft
import scipy.signal as signal
import matplotlib.pyplot as plt

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
#print("# Samples: ",N)
#print ('# Sample time :',T)


#Compute an plot FFT
plt.figure(2)  
xf = np.linspace(0.0, 1.0/(2.0*T), num = np.int32(N/2))
yf = fft.fft(x)
plt.plot(xf, 2.0/N * np.abs(yf[0:np.int32(N/2)]))
plt.grid()
plt.xlabel('Frequency (Hz)')
plt.ylabel('Accel (g)')
plt.title('FFT - Mesin Mobil')

########################################################
# Kita akan membuat highpass filter 
# kita akan membuag sinyal dibawah 500 Hz
# Jadi frekuensi cutoff adalah 500 Hz
########################################################

numtap = 21
fc = 500

#Hitung nilai frekuensi cutoff ternormalisasi
phi_c = 2*np.pi* fc * T

#Menggunakan firwin
b_coeff = signal.firwin(numtap,phi_c,pass_zero='highpass')
ws, hs = signal.freqz(b_coeff)

#Amplitudo dalam db
amp_db = 20*np.log10(np.abs(hs))

plt.figure(3)
plt.plot(ws,amp_db, 'b')
plt.xlabel('Frequency (rad)')
plt.ylabel('Amplitudo (dB)')
plt.grid()
plt.show()

#Print b_coeff
print('Koefisien filter : ')
print(b_coeff)

######################################################################
# Kita sudah punya koeffisien index filter
# Kita implementasikan dengan direct form
# dengan menggunakan lfilter
######################################################################

y_filtered = signal.lfilter(b_coeff, [1], x)
    
################################
# Plot sinyal hasil filter
################################
plt.figure(4)
plt.plot(t,y_filtered, 'b')
plt.xlabel('Time')
plt.ylabel('Amplitudo')
plt.grid()
plt.show()

###################################
# Plot FFT setelah di filter
###################################

N = np.int32(np.prod(t.shape))
plt.figure(5)  
xf = np.linspace(0.0, 1.0/(2.0*T), num = np.int32(N/2))
yf = fft.fft(y_filtered)
plt.plot(xf, 2.0/N * np.abs(yf[0:np.int32(N/2)]))
plt.grid()
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitudo')
