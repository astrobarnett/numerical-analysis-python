#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:11:58 2020

@author: astro
"""
import math

N = int(1e+5)  #number of steps
a = 0. # initial limit of integration
g = 6.67408e-11
sigma = 1e4 #m/s
fakh = 0.
DDF = int(input("Choose the Density Distribution Function (1 - SIS; 2 - NFW): "))

if(DDF==1):   
    b = 3.08567758130573e17 # final limit of integration
    h = (b-a)/N # size in the X axis for each trapezoid 
    roa = float((sigma**2.)/(2.*math.pi*g)) # eqn 103 exercise
    rob = float((sigma**2.)/(2.*math.pi*g)) # eqn 103 exercise
    fa = float(4.*math.pi*roa) #calculates function for initial limit a
    fb = float(4.*math.pi*rob)#calculates function for final limit b
    
    for k in range(1, N-1):
        fakh+=float(4.*math.pi*roa)
        # calculates sum of function for (a+k*h), where k goes from 1 to N-1 
    I = float(h*((0.5*fa)+(0.5*fb)+(fakh)))
    I=I/(1.989e30) #divided by solar mass
    
if(DDF==2):    
    ro0 = 1e8 #normalization (mass/vol) solar mass
    rs = 10. #scale radius 
    b = 100.*rs #r-max
    h = (b-a)/N
    rob=float((ro0)/((b/rs)*((1+(b/rs))**2))) # equation 104 of exercie 
    fb = float((4*math.pi*rob*(b**2))) # put above qn in eqn 102
                    
    for k in range(1, N-1):
        c = (a+k*h)
        roakh=float((ro0)/((c/rs)*((1+(c/rs))**2))) 
        fakh+=float((4*math.pi*roakh*(c**2)))
            
    I = float(h*((0.5*fb)+fakh))

print(I, 'Solar masses')
