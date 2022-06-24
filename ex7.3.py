#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:11:58 2020

@author: astro
"""
import math
import random
import matplotlib.pyplot as plt

#%% Integral

N = [1e3, 5*1e3, 1e4, 5*1e4, 1e5, 5*1e5, 1e6, 5*1e6]
I = []
Ip = 0.

for v in range(int(len(N))):
    for i in range(int(N[v])):
        x = random.random()*2.#draws a random uniform number between the limits
        y = float((math.sin(1./(x*(2.-x))))**2.) #equation for the given function
        Ip+=y #repeats it for N times and sums up all results
    I.append((2./N[v])*Ip)# I = Ip*(b - a)/N
    Ip = 0.
        
print(I)
M=((I[0]+I[1]+I[2]+I[3]+I[4]+I[5]+I[6]+I[7])/8)
print('Averange integral value: ', M)

#%% Plot

plt.plot(N, I) 
plt.xlabel('N', fontsize=20)
plt.ylabel('I', fontsize=20)
plt.xscale('log')
plt.show()
