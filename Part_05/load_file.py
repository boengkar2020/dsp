#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:42:56 2022

@author: sukarno
"""

import matplotlib.pyplot as plt
import numpy as np


t, x = np.genfromtxt('mesin_mobil.csv',delimiter=',', unpack=True)

#Plot data
plt.figure(1)  
plt.plot(t, x)
plt.xlabel('Time (seconds)')
plt.ylabel('Accel (g)')
plt.title('Mesin Mobil')
plt.grid()
