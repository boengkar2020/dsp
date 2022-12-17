#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 21:58:48 2022

@author: sukarno
"""

import numpy as np
import scipy.fft as fft
import scipy.signal as signal
import matplotlib.pyplot as plt

def gen_dt_signal(n,T):
    t = n * T
    sig = np.sin(1.2*2*np.pi*t)
    noise = 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)
    return sig + noise

Fs = 100 #frekuensi sampling
Ts = 1/Fs # T sampling

ns = np.arange(0, 1000)
data = gen_dt_signal(ns,Ts)

plt.figure(1)
plt.plot(ns,data, 'b')
plt.xlabel('Time')
plt.ylabel('Amplitudo')
plt.grid()
plt.show()


#Plot  FFT
N = np.int32(np.prod(ns.shape))
plt.figure(2)  
xf = np.linspace(0.0, 1.0/(2.0*Ts), num = np.int32(N/2))
yf = fft.fft(data)
plt.plot(xf, 2.0/N * np.abs(yf[0:np.int32(N/2)]))
plt.grid()
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitudo')


########################################################
# Sinyal utama adalah 1,2 Hz
# dan kita akan membuang sinyal noise di atas 1,2 Hz
# Kita tetakan misalkan frekuensi cutoff = 2Hz
########################################################

numtap = 41
fc = 2

#Hitung nilai frekuensi cutoff ternormalisasi
phi_c = 2*np.pi* fc * Ts

#Menggunakan firwin
b_coeff = signal.firwin(numtap,phi_c)
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
## y(n) = 0.0327602 x(n) +  0.23955829 x(n-1) +  0.45536302 x(n-2) + 
## 0.23955829 x(n-3) +  0.0327602 x(n-4)
######################################################################


class RingBuffer:
    def __init__ (self,N):
        self.__buf = np.zeros(N)
        self.__maxN = N
        
    def append(self,x):
        
        self.__buf = np.append([x],self.__buf)
        self.__buf = self.__buf[0:self.__maxN]

    def get(self):
        return self.__buf


#def yn(b,x):
   # return b*x

##########################################################
# Kita implementasikan
# Pengunaan ring buffer berguna jika data input realtime
##########################################################


rb = RingBuffer(numtap)


y_filtered = np.array([])

for n in np.arange(np.int32(np.prod(data.shape))):
    
    y_sum = 0
    rb.append(data[n])
    shift_xs = rb.get()
    
    for k in np.arange(numtap):
        y_sum += b_coeff[k] * shift_xs[k]
        
    y_filtered  = np.append(y_filtered,[y_sum])
    

################################
# Plot sinyal hasil filter
################################
plt.figure(4)
plt.plot(ns,y_filtered, 'b')
plt.xlabel('Time')
plt.ylabel('Amplitudo')
plt.grid()
plt.show()


###################################
# Plot FFT setelah di filter
###################################

N = np.int32(np.prod(ns.shape))
plt.figure(5)  
xf = np.linspace(0.0, 1.0/(2.0*Ts), num = np.int32(N/2))
yf = fft.fft(y_filtered)
plt.plot(xf, 2.0/N * np.abs(yf[0:np.int32(N/2)]))
plt.grid()
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitudo')