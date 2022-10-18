#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 09:04:34 2022

@author: sukarno
"""

import matplotlib.pyplot as plt
import math

def nrange (min, max, delta = 1):
    last_data = min
    data = [last_data]
    
    while last_data <= max:
        last_data += delta
        data.append(last_data)
        
    return data

def u(n) :
    return 1 if n >= 0 else 0

def f(A, n) :
    return A * math.cos(0.125*math.pi*n) * u(n)


A = 1

xn = nrange(-10,13)

yn = [f(A,n) for n in xn]

fig, ax = plt.subplots()

ax.vlines(xn,0,yn)
ax.grid()

plt.show()