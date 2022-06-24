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
I = [] #integral array 
k = 0.

for v in range(int(len(N))):
    for i in range(int(N[v])):
        x = random.random()*2 #generate uniform random point (x, y)
        y = random.random() #inside the limit (2, 1) coz area of the rectangle 2x1=2 
        f = float((math.sin(1/(x*(2-x))))**2) #calculate y with random x
        if (f>=y): #if generated point is below calculated point, add 1 counter
            k+=1 #repeat for N times
    I.append((k/N[v])*2) #Integral equals to k times area divided by N generated points
    k=0
print(I)
M=((I[0]+I[1]+I[2]+I[3]+I[4]+I[5]+I[6]+I[7])/8)
print('Averange integral value: ', M)

#%% Plot

plt.plot(N, I) 
plt.xlabel('N', fontsize=10)
plt.ylabel('I', fontsize=10)
plt.xscale('log')
plt.show()
