#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 17:33:03 2022

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


def f(A,t,freq):
    return A * math.sin(2 * math.pi * t * freq)

def f_sampling(A,n,fs):
    return A * math.sin(2 * math.pi * n * fs)

if __name__ == '__main__':

    A = float(input("Masukan amplitudo (V) : "))
    freq = float(input("Masukan Frequensi (Hz) : "))
    
    T = 1 / freq
    
    fig, ax = plt.subplots()
    
    x = nrange(0, 1,T)
    y = [f_sampling(1, n, 1) for n in x]
    ax.vlines(x,0,y)
    ax.grid()
    
    plt.show()