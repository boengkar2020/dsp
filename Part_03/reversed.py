#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 22:31:02 2022

@author: sukarno

Reversed and shift
"""

import matplotlib.pyplot as plt
import numpy as np


def h(k):
    
    if k in [0,1]:
        return 3
    elif k in [2,3]:
        return 1
    
    return 0

if __name__ == '__main__':
    
    ks = np.arange(-5,6)
    
    hs = [h(4-k) for k in ks]
    
    fig, ax = plt.subplots()

    ax.stem(ks,hs)
    ax.grid()

    plt.show()