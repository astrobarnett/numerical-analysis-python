#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:11:58 2020

@author: astro
"""
import random
import math
import matplotlib.pyplot as plt

N = int(1e4)
sig = 2
mmax = 50.
mmin = -50.
X = []
k = 0

while (k<N):
    a=random.random()
    z = a*(mmax-mmin)+mmin # uniform random number within max and min
    m=random.random() # uniform random number between 0 and 1
    p = (1/(2*math.pi)**0.5/sig*math.exp(-z**2/2/sig**2))
    #calculate gaussian distribution using the 1st random number y
    if (m<=p):
        X.append(z) #if random m is smaller than the gaussian, add it to list
        k+=1 #that means the value is inside our desired distribution
#keeps up until it has the chosen number N of gaussian distributions added to list
        
plt.hist(X,bins=60,density='True')
plt.xlabel("x")
plt.ylabel("PDF(x)")
plt.show()    
