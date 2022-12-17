#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 22:26:56 2022

@author: sukarno
"""

from scipy.signal import convolve, residue


denom = convolve([1,-1],[1,-0.5])

print("-- denom --")
print(denom)

[R,P,K] = residue([1,0],denom)
print("-- RPK --")
print(R)
print(P)
print(K)