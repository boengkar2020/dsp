#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:18:34 2022

@author: sukarno
"""

import matplotlib.pyplot as plt
import numpy as np


def u(n) :
    return 1 if n >=0 else 0

def h(k) :
    return (0.25**k) * u(k)

def x(k):
    return u(k)


def y(n,ks) :
    
    yn = 0
    for k in ks:
        yn += x(k) * h(n - k)
        
    return yn

def plot_graph (xs,ys):
    
    fig, ax = plt.subplots()

    ax.stem(xs,ys)
    ax.grid()

    plt.show()
    

if __name__ == '__main__':
    
    #Deret k
    ks = np.arange(-5,6)
    
    #hasil h(k)
    hs =[h(k) for k in ks]
    #hasil x(k)
    xs = [x(k) for k in ks]
    
    #Plot
    plot_graph(ks, hs)
    plot_graph(ks, xs)
    
    #Deret n
    ns = np.arange(0,10)
    
    print("\n\n---------------------------------\n")
    for n in ns:
        print("n = {0} -> y({1}) = {2} \n".format(n,n,y(n,ks)))
        
    print("\n\n---------------------------------\n")
    
    ys = [y(n,ks) for n in ns]
    
    plot_graph(ns, ys)