#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 16:11:58 2019

@author: astro
"""
import numpy as np

a = np.array([[2., 1., 4., 1.], [3., 4., -1., -1.], [1., -4., 1., 5.], [2., -2., 1., 3.]])
r = np.array([[-4.], [3.], [9.], [7.]])

for j in range(len(a)): #for loop for array a 
    for i in range(len(a[0])):
        if(i==j): # condition for diagonal element
            r[i]=r[i]/a[i][j] #divide a row by its diagonal element to obtain Aij=1
            a[i]=a[i]/a[i][j] #divide a row by its diagonal element to obtain Aij=1
        if(i>j):
            r[i]=r[i]-((a[i][j]/a[j][j])*(r[j]))
            a[i]=a[i]-((a[i][j]/a[j][j])*(a[j]))

v = np.zeros([len(a),1],float) #arrays 
#Ax=b to solve by backsubstitution,    
v[3] = r[3] # b3=z
v[2] = r[2]-(v[3]*(a[2][3])) # b2=y+ A23*z
v[1] = r[1]-(v[3]*(a[1][3]))-(v[2]*(a[1][2])) #b1=x + A12*y + A13*z  
v[0] = r[0]-(v[3]*(a[0][3]))-(v[2]*(a[0][2]))-(v[1]*(a[0][1])) #b0=w + A01*x + A02*y + A03*z 

print(v)
