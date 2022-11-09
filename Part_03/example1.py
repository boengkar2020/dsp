#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 23:02:11 2022

@author: sukarno
"""


import matplotlib.pyplot as plt
import numpy as np

def h(k):
    
    if k == 0:
        return 3
    elif k == 1:
        return 2
    elif k == 2:
        return 1
    
    return 0

def x(k):
    
    if k == 0:
        return 3
    elif k == 1 :
        return 1
    elif k == 2:
        return 2
    
    return 0

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
    
    ks = np.arange(-5,6)
    
    hs =[h(k) for k in ks]
    xs = [x(k) for k in ks]
    
    #Plot
    plot_graph(ks, hs)
    plot_graph(ks, xs)
    
    ns = np.arange(0,10)
    
    print("\n\n---------------------------------\n")
    for n in ns:
        print("n = {0} -> y({1}) = {2} \n".format(n,n,y(n,ks)))
        
    print("\n\n---------------------------------\n")
    
    ys = [y(n,ks) for n in ns]
    
    plot_graph(ns, ys)
    