#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 19:06:20 2019

@author: astro
"""

from math import sin
import numpy as np
import matplotlib.pyplot as plt
 
# for legend
fig = plt.figure()
ax = plt.subplot(111)

#Define function
def f(x,t):
    return -x**3+sin(t)

a=0.0    #start of interval
b=100.0   #End of interval
N=1000    #Number of steps 
h=(b-a)/N  #size of a single step


################################### Euler method


euler =np.arange(a,b,h)
eul=[]
x=0.0 #initial condition
for t in euler:
    eul.append(x)
    x+=h*f(x,t)
ax.plot(euler,eul,'k+',label='Euler')   

######################################rk2 method



srk =np.arange(a,b,h)
mid = []
x=0.0 #initial condition
for t in srk:
    mid.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    x += k2
ax.plot(srk,mid,'g*',label='Midpoint')     

######################################## Rk4 method 

tpoints =np.arange(a,b,h)
xpoints = []
x = 0.0 #initial condition
for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6
ax.plot(tpoints,xpoints,'r-',label='RK4')

#### for the graph 

plt.xlabel("t")
plt.ylabel("x(t)")
ax.legend()
ax.legend(loc='upper right')
plt.show()



























 
