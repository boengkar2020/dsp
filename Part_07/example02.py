#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 21:07:30 2022

@author: sukarno
"""

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

#Menggunakan firwin
b_coeff = signal.firwin(9,0.000125,window="hamming")
ws, hs = signal.freqz(b_coeff)

#Amplitudo dalam db
amp_db = 20*np.log10(np.abs(hs))

plt.figure(1)
plt.plot(ws,amp_db, 'b')
plt.xlabel('Frequency (rad)')
plt.ylabel('Amplitudo')
plt.grid()
plt.show()

'''
#Menggunakan firwin2
b_coeff = signal.firwin2(41,[0, 0.000125,0.25,1.0],[1,1,0,0])

ws, hs = signal.freqz(b_coeff)

#Amplitudo dalam db
amp_db = 20*np.log10(np.abs(hs))

plt.figure(2)
plt.plot(ws,amp_db, 'b')
plt.xlabel('Frequency (rad)')
plt.ylabel('Amplitudo')
plt.grid()
plt.show()
'''




