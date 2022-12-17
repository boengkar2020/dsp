#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:35:02 2022

@author: sukarno
"""

import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt

xn = [1,2,3,4,1]

N = 5

ks = [k for k in range(0, N) ]
Xk = fft(xn)
#print(Xk)
Ak = [np.abs(Xk[k]) * (1/N)  for k in range(0, N) ]

print(Ak)
    
plt.figure(1) 
plt.stem(ks,Ak)
plt.grid()