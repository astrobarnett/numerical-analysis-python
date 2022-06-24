#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 15:11:48 2019

@author: astro
"""

import numpy as np
import math as m

h=1e-6
def f(x):
    f=x-F-ecc*np.sin(x)
    return(f)

        
tol=1e-6
E=300
Eold=2
mano=input('choose a value for mean anomaly between pi or pi/3: ')
if(mano=='pi'):
    F=np.pi
if(mano=='pi/3'):
    F=np.pi/3

ecc=float(input('choose a value for eccentricity between 0.1, 0.7 or 0.9: '))

while(abs(Eold-E)>tol): #iteration
    
    Eold=E
    g=(f(E+h/2)-f(E-h/2))/h #central difference
    E=E-f(E)/g
    
    print(g,1-ecc*np.cos(E))
    
    
print('\nFor mean anomaly equal to',F,', the eccentricity anomaly E=',E)
