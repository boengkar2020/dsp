#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 23:13:08 2022

@author: sukarno
"""

from scipy.signal import convolve, residue

nom = convolve([1,0,0],[1,1])

print(nom)

denom = convolve([1,-1],[1,-1,0.5])

print(denom)

[R,P,K] = residue([1,1,0],denom)
print("-- RPK --")
print(R)
print(P)
print(K)