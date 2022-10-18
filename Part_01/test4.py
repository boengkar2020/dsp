#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 10:31:22 2022

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

#Fungsi step
def u(n):
    return 1 if n >= 0 else 0


#fungsi sinyal
#def x(n):
    #return 10 * math.exp(-5 * (10**(-3)) * n) * u(n)

#fungsi sinyal
def x(n):
    return 10 * math.sin(2 * (10**(-3)) * math.pi * n) * u(n)

if __name__ == '__main__' :
    
    ns = nrange(0.0, 1000.0)
    y = [ x(n) for n in ns]
    
    fig, ax = plt.subplots()
    
    #Plot Sampling nya
    #ax.vlines(ns,0,y)
    
    #Rekonstruksi
    ax.plot(ns,y)
    
    ax.grid()

    plt.show()