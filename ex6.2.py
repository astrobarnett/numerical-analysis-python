#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:11:58 2020

@author: astro
"""

import numpy as np
from numpy import random
import matplotlib.pyplot as plot

N=100000

#inizializzazione delle variabile dove memorizzare i valori

r=np.zeros(N,float)
t=np.zeros(N,float)
x=np.zeros(N,float)
y=np.zeros(N,float)
Pr=np.zeros(N,float)
Pt=np.zeros(N,float)

sigma=2.

for i in range(N):

    #seed identifier of the random sequence
    random.seed(None)

    #generation of r and theta  
    Pr[i]=np.random.rand()
    
    r[i]=(-2*(sigma**2)*np.log(1-Pr[i]))**0.5

    Pt[i]=np.random.rand()
    
    t[i]=2*np.pi*(Pt[i])
    

#calculation of the values ​​of x and y, random variables independent of each other, normally distributed
    
    x[i]=r[i]*np.cos(t[i])
    
    y[i]=r[i]*np.sin(t[i])
    
    
plot.hist(x,bins=60, histtype='bar')
plot.hist(y,bins=60, histtype='step')
plot.xlabel('$x$',fontsize=12)
plot.ylabel('$PDF(x)$',fontsize=12)



plot.show()
