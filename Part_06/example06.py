#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 23:06:40 2022

Memplot frekuensi response dari sebuah sistem H(z)

@author: sukarno
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import freqz


#Plot data soal A
plt.figure(1)  
w,h = freqz([1],[1,-0.5],1024)
plt.plot(w,np.abs(h), 'b')
plt.xlabel('Frequency (rad)')
plt.ylabel('Magnitude')
plt.grid()
ax1 = plt.twinx()
ax1.plot(w,np.unwrap(np.angle(h)), 'g')
ax1.set_ylabel('Phase')


#plot data soal B
plt.figure(2)  
w,h = freqz([1,-0.5],[1],1024)
plt.plot(w,np.abs(h))
plt.xlabel('Frequency (rad)')
plt.ylabel('Magnitude')
plt.grid()
ax1 = plt.twinx()
ax1.plot(w,np.unwrap(np.angle(h)), 'g')
ax1.set_ylabel('Phase')

#plot data soal C
plt.figure(3)  
w,h = freqz([0.5, 0, -0.32],[1 , -0.5, 0.25],1024)
plt.plot(w,np.abs(h))
plt.xlabel('Frequency (rad)')
plt.ylabel('Magnitude')
plt.grid()
ax1 = plt.twinx()
ax1.plot(w,np.unwrap(np.angle(h)), 'g')
ax1.set_ylabel('Phase')

#plot data soal D
plt.figure(4)  
w,h = freqz([1 ,-0.9 , 0.81],[1 , -0.6, 0.36],1024)
plt.plot(w,np.abs(h))
plt.xlabel('Frequency (rad)')
plt.ylabel('Magnitude')
plt.grid()
ax1 = plt.twinx()
ax1.plot(w,np.unwrap(np.angle(h)), 'g')
ax1.set_ylabel('Phase')


