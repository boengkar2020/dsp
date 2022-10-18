#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:52:18 2022

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



def f_discrete(A,n,T,freq):
    return A * math.sin(2 * math.pi * n * T * freq)


if __name__ == '__main__':

    A = float(input("Masukan amplitudo (V) : "))
    freq = float(input("Masukan Frequensi (Hz) : "))
    freq_s = float(input("Masukan Frequensi Sampling(Hz) : "))
    
    T = 1/freq_s
    
    fig, ax = plt.subplots()
    
    x = nrange(0, freq_s - 1)
    
    y = [f_discrete(A, n, T, freq) for n in x]
    
    ax.vlines(x,0,y)
    ax.grid()
    
    plt.show()