#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 22:31:22 2019

@author: astro
"""
import math 
g=9.81
t=float(input("Enter the time for falling ball t:"))
d = 0.5*g*t**2    #eqn of motion s=gt^2/2 
h=float(input("Enter the height:"))
t2=math.sqrt(2*h/g) #eqn of motion s=ut+0.5*g*t^2 
print("The distance covered is:", d)
print("The time it took is:", t2)

