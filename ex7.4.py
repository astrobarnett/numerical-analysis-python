#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:11:58 2020

@author: astro
"""
import math
import random

N = [1e3, 5*1e3, 1e4, 5*1e4, 1e5, 5*1e5, 1e6, 5*1e6]
I = []
Ip = 0.
DDF = int(input("Choose the Density Distribution Function (1 - SIS; 2 - NFW): "))

if(DDF==1):    
    g = 6.67408e-11
    sigma = 1e4 #m/s
    b = 3.08567758130573e17
    ro = float((sigma**2.)/(2.*math.pi*g)) 
    for v in range(int(len(N))):
        for i in range(int(N[v])):            
            y = float(4.*math.pi*ro) #constant function, no need for random number
            Ip+=y #repeats calculation N times and sums up all results
        I.append(((b/N[v])*Ip)/1.989e30) # Integral = Ip * (b-a)/N
        Ip = 0.
        
if(DDF==2):   
    ro0 = 1e8 #normalization (mass/vol) solar mass
    rs = 10. #scale radius 
    b = 100.*rs #r-max
    for v in range(int(len(N))):
        for i in range(int(N[v])):
            x = random.random()*b  #produces a uniform random number
            ro=float((ro0)/((x/rs)*((1+(x/rs))**2))) # equation 104 of exercie 7.1            
            y = float((4*math.pi*ro*(x**2))) #apply it to the function eqn 102 of ex 7.1
            Ip+=y  #generates N numbers and sum all of them
        I.append((b/N[v])*Ip) # Integral = Ip * (b-a)/N
        Ip = 0.
       
print(I)
M=((I[0]+I[1]+I[2]+I[3]+I[4]+I[5]+I[6]+I[7])/8)
print('Averange integral value: ', M, 'Solar masses')
