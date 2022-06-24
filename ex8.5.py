#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:11:58 2020

@author: astro
"""

import math
import numpy as np
import matplotlib.pyplot as plt


g = 9.81


# Definition of functions
def euler( t0, h, t, x0, x, v0 ):
	k = x0 
	w = v0
	list_x = []
	list_t = []
	list_v = []
	list_x.append(x0)
	list_t.append(t0)
	list_v.append(v0)
	while t0 < t:
		w = w - h * g
		k = k + h * w
		t0 = t0 + h 
		list_x.append(k)
		list_t.append(t0)
		list_v.append(w)
	return (list_t,list_x,list_v)

#initial conditions
t0 = 0
x0 = 0
h = 1/1000
v0=0
tolerance=0.001


# Value of x at which we need approximation 
t = 3
x = 10

(tt, xx, vv) = euler(t0, h, t, x0, x, v0) 


while(abs(xx[-1]-x)>tolerance):

	v0 +=0.001

	(tt, xx, vv) = euler(t0, h, t, x0, x, v0)



plt.plot(tt, xx , color="blue", linestyle="-" , label= '$x(t)$')
plt.plot(tt, vv , color="red", linestyle="-" , label= '$v(t)$')
plt.axis([0,3,-20,20])
plt.xlabel("time (code units)", fontsize=12)
plt.ylabel("half-mass radius (pc)", fontsize=12)
plt.legend(loc = "lower left", fontsize=8)
plt.show()

