#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 23:38:44 2022

@author: sukarno
"""

import numpy as np
from scipy.fft import fft, ifft


def wn(N):
    return complex(np.cos((2 * np.pi) / N),  - np.sin((2 * np.pi) / N))

#DFT
def X(k,xn):
    N = len(xn)
    
    sum_ck = 0
    for n in range(0,N):
        sum_ck += xn[n] * (wn(N)** (k *n))
        
    return sum_ck

#inverse DFT
def x(n,xk):
    N = len(xk)
    
    sum_cn = 0
    for k in range(0,N):
        sum_cn += xk[k] * (wn(N)** (k * n * -1))
        
    return (1/N) * sum_cn
    
xs = [1,2,3,4]
#Hitung secara manual
for k in range(0,len(xs)):
    ck = X(k,xs)
    print("X({0}) -> {1}".format(k,ck))
    

#menggunakan fungsi fft 
# FFT
Xk = fft(xs)
#print(Xk)

#inverse FFT
xn = ifft(Xk)
print(xn)

    
