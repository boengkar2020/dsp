#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:09:19 2022

@author: sukarno
"""

import matplotlib.pyplot as plt
import numpy as np
import math


# x(n) = sin(0.5PIn)
FS = 4
PERIODIC = 1

def x(n) :
    return math.sin(0.5 * math.pi * n)

def c(k,xn):
    N = len(xn)
    n_sum = 0
    for n in range(0,N):
        n_sum += xn[n] * np.exp( -1j * ((2 * math.pi * k * n) / N))
        
    cpx = (1/N) * n_sum
    
    return complex(np.int32(cpx.real), cpx.imag)


#ns = np.arange(0,(FS * PERIODIC) + 1)
#xs = [ np.int32(x(n)) for n in ns ]
#plt.figure(1) 
#plt.stem(ns,xs)
#plt.plot(ns,xs)
#plt.title('Plot Sinyal')
#plt.grid()

ns = np.arange(0,FS)
xn = [np.int32(x(n)) for n in ns]
#print(xn)

for k in range(0,len(xn)):
    ck = c(k,xn)
    print("C{0} -> {1}".format(k,ck))
