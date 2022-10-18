#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 21:16:00 2022

@author: sukarno
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from scipy import signal
import matplotlib.pyplot as plt
import math

x_label = 'time (s)'
y_label = 'voltage (mv)'
chart_title = 'Simple sinus wave'

def nrange (min, max, delta = 1):
    last_data = min
    data = [last_data]
    
    while last_data <= max:
        last_data += delta
        data.append(last_data)
        
    return data


def f(A,t,freq):
    return A * math.sin(2 * math.pi * t * freq)

def fs(A,n,freq):
    return A * math.sin(2 * math.pi * n * freq)

if __name__ == '__main__':
    A = float(input("Masukan amplitudo (mv) : "))
    freq = float(input("Masukan frequensi (Hz) : "))
    freq_s = float(input("Masukan frequensi sampling (Hz) : "))
    
    dt = 1 / (100 * freq)
    #ds = 1 /  freq_s
    ds = 1 /  (100 * freq_s)
    
    x = nrange(0.0, 1.0,dt)
    xs = nrange(0.0, 1.0,ds)
    
    y = [f(A,t,freq) for t in x]
    
    ys = [fs(A,n,freq_s) for n in xs]

    fig, ax = plt.subplots()
    
    ax.plot(x, y)
    #ax.vlines(xs, 0, ys,colors="r")
    ax.plot(xs,ys)

    ax.set(xlabel=x_label, ylabel=y_label,
           title=chart_title)
    
    ax.grid()

    plt.show()