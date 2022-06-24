#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 15:11:48 2019

@author: astro
"""
import numpy as np
import math as mt

ecc=float(input('Enter the value of the eccentricity (0.1, 0.7, 0.9):'))
F1= mt.pi #result for pi
F2= mt.pi/3 #result for pi/3
#F=x-ecc*np.sin(x), x=E
tot=1e-6

ival=int(input('Choose the method: relaxation(1), bisection (2), Newton-Rapshon (3):'))

#relaxation method
if(ival==1):
    x3=1. #guess
    x=1.
    xold=10.

    while(abs(x3-xold)>tot): #iteration
        xold=x3
        x3=F1+ecc*np.sin(x3)
    print('For F=F1 Converged to E=',x3)
    
    while(abs(x-xold)>tot): #iteration
        xold=x
        x=F2+ecc*np.sin(x)
    print('For F=F2 converged to E=',x)
                
#bisection method
if(ival==2):
    x1=0
    x2=1.
    xmid=0
    xmid1=0
    while(5>0):
        f1=x1-ecc*np.sin(x1)-F1
        f2=x2-ecc*np.sin(x2)-F1
        if(f1*f2<0):
            break
        x2 += 1
    print(x1,x2)

    while(abs(x2-x1)>tot): #iteration
        xmid=0.5*(x2+x1)
        fmid=xmid-ecc*np.sin(xmid)-F1
        f1=x1-ecc*np.sin(x1)-F1
        if(f1<0 and fmid>0):
            x1=x1
            x2=xmid
        else:
            x1=xmid
            x2=x2
    print('For F1, it converges at E=',xmid)
    #F=F2
    x1=0. #riassegnazione
    x2=1.
    while(5>0):
        f1=x1-ecc*np.sin(x1)-F2
        f2=x2-ecc*np.sin(x2)-F2
        if(f1*f2<0):
            break
        x2 += 1
    print(x1,x2)

    while(abs(x2-x1)>tot): #iteration
        xmid1=0.5*(x2+x1)
        fmid=xmid1-ecc*np.sin(xmid1)-F2
        f1=x1-ecc*np.sin(x1)-F2
        if(f1<0 and fmid>0):
            x1=x1
            x2=xmid1
        else:
            x1=xmid1
            x2=x2
    print('For F2, it converges at E=',xmid1)
    #1) x-ecc*np.sin(x)-F=0
    #2) choose the interval x1, x2
    #3) calculate f(x1) and f(x2)
    #4) compare them to continue the research
    #5) choose when to stop iterate:abs(x2-x1)>1e-6

#Newton-Rapshon method
if(ival==3):  #f'(x)= 1 - ecc*cos(x)
    x=1.
    xnew=0.
    while(5>0):
        f=x-ecc*np.sin(x)-F1
        f1=1-ecc*np.cos(x)  #real derivative
        deltax=f/f1
        xnew=x-deltax
        if(abs(xnew-x)<=tot):
            break
        x=xnew  #reassignment
        
    print('For F1, it converges at E=', x)
    #F=F2
    x=1.
    xnew=0.
    while(5>0):
        f=x-ecc*np.sin(x)-F2
        f1=1-ecc*np.cos(x)  #real derivative
        deltax=f/f1
        xnew=x-deltax
        if(abs(xnew-x)<=tot):
            break
        x=xnew  #reassignment
        
    print('For F2, it converges at E=', x)
