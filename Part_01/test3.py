#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 08:34:52 2022

@author: sukarno
"""

#Sinyal Analog


import matplotlib.pyplot as plt
import math

def nrange (min, max, delta = 1):
    last_data = min
    data = [last_data]
    
    while last_data <= max:
        last_data += delta
        data.append(last_data)
        
    return data

def u(n):
    return 1 if n >= 0 else 0


#def x(n):
    #return 10*math.exp(-625 * (10**-3) * n)  * u(n)

def x(n):
    return 10*math.sin(0.25 * math.pi * n)  * u(n)

if __name__ == '__main__':
    
    #Asalanya dari frekuensi sampling dibagi 2
    
    ts = nrange(0.0, 10.0)
    y = [x(n) for n in ts]
    
    fig, ax = plt.subplots()
    
    #Plot Sampling nya
    ax.vlines(ts,0,y)
    
    #Plot rekonstruksi
    #ax.plot(ts, y)
    
    ax.grid()

    plt.show()