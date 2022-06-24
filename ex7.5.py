#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:11:58 2020

@author: astro
"""
import random
import math
import matplotlib.pyplot as plt

N = [1e3, 5*1e3, 1e4, 5*1e4, 1e5, 5*1e5, 1e6, 5*1e6]
fxwx = 0.
Ip = 0.
I = []
I1 = []

for v in range(int(len(N))):
    for i in range(int(N[v])):
        y = random.random()
        x = y**2    #solved eqn 124 in notes
        fxwx+=1./(math.exp(x)+1.)    #inserts weighted random number in f(x)/w(x)
    I.append((2.*fxwx)/N[v]) # I = (1/N) * fxwx * int(w(x)) see formula for importance sampling 
    fxwx = 0.    #int((w(x))) = 2
    #repeats sum for N times

#I1 for mean value       
for k in range(int(len(N))):
    for j in range(int(N[k])):
        x = random.random() #draws a random uniform number
        y = float(x**(-0.5)/(math.exp(x)+1.)) #equation for the given function
        Ip+=y #repeats it for N times and sums up all results
    I1.append((1/N[k])*Ip) # I = Ip*(b - a)/N
    Ip = 0.
     
M1=((I1[0]+I1[1]+I1[2]+I1[3]+I1[4]+I1[5]+I1[6]+I1[7])/8)
M=((I[0]+I[1]+I[2]+I[3]+I[4]+I[5]+I[6]+I[7])/8)
print('Averange integral value: ', M1, '(Mean Value); ', M, '(Importance).')      

plt.plot(N, I, color='r', marker='o') # for importance sampling 
plt.plot(N, I1, color='b', marker='*') # for mean value method 
plt.xlabel('N', fontsize=20)
plt.ylabel('I', fontsize=20)
plt.xscale('log')
plt.show()
