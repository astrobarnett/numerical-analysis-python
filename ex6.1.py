#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 5 15:11:48 2020

@author: astro
"""

import random
import math
import matplotlib.pyplot as plt

N = int(1e7)
a = 1-2.3
mmax = 150. #max solar mass
mmin = 0.1 #min solar mass 
Y = []

for i in range(N):
    x=random.random()   #generates a random number with uniform distribution
    y = (x*(mmax**a-mmin**a)+mmin**a)**(1./a) 
    # after normalazing and integrating p(x)dx in the max and
    # min limits, we obtain the distribution formula, where
    # we insert the uniform random numbers.
    y = math.log10(y)   #log10 scale
    Y.append(y) 
    
plt.hist(Y,bins=30,histtype='step',log=True)    #plots histogram

plt.xlabel('M($M_\odot$)', fontsize=15)

#plt.label('dN/dlogM', fontsize=15)


plt.show()    
