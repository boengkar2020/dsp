#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:25:02 2022

@author: sukarno
"""
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

b_coeff = np.array([0.1871,0.2,0.1871])

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
#Tambakan window function, mungkin bisa memperbaiki response
w_funcs = signal.get_window('hamming',3)
#w_funcs = signal.get_window(('kaiser',2.70),3)

bw_coeff = b_coeff * w_funcs

ws, hs = signal.freqz(bw_coeff)

#Amplitudo dalam db
amp_db = 20*np.log10(np.abs(hs))

plt.figure(2)
plt.plot(ws,amp_db, 'b')
plt.xlabel('Frequency (rad)')
plt.ylabel('Amplitudo')
plt.grid()
plt.show()
'''
