#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:11:48 2019

@author: astro
"""
import numpy as np

a = np.array([[4., -1., -1., -1.], [-1., 3., 0., -1.], [-1., 0., 3., -1.], [-1., -1., -1., 4.]])
r = np.array([[1.], [0.], [1.], [0.]]) * 5

x = np.zeros((len(a), 1), float) #transform a into an array x
z = np.zeros((len(a), 1), float) #transform b into an array z
diff= 100.

method = int(input('Select the method (1 - Gauss elim.; 2 - Gauss-Seidel): '))

if(method==1):
    for j in range(len(a)): #for loop for array a
        for i in range(len(a[0])):
            if(i==j): # condition for diagonal element
                r[i]=r[i]/a[i][j] #divide a row by its diagonal element to obtain Aij=1
                a[i]=a[i]/a[i][j] #divide a row by its diagonal element to obtain Aij=1
            if(i>j):
                r[i]=r[i]-((a[i][j]/a[j][j])*(r[j])) 
                a[i]=a[i]-((a[i][j]/a[j][j])*(a[j])) 
    
    v = np.zeros([len(a),1],float)   
    v[3] = r[3]
    v[2] = r[2]-(v[3]*(a[2][3]))
    v[1] = r[1]-(v[3]*(a[1][3]))-(v[2]*(a[1][2]))
    v[0] = r[0]-(v[3]*(a[0][3]))-(v[2]*(a[0][2]))-(v[1]*(a[0][1]))
    print(v)
 
if(method==2):        
    while(diff>1e-4):
        for i in range(len(r)): #for loop in r 
            c = 0.0 # initial value for the diagonal term
            for j in range(len(r)): #for loop in r 
                if (j != i): #if col(j) not equal to row(i)
                     c += a[i][j]*x[j]  #Extract the diagonal terms from the sum      
            z[i] = (r[i]-c)/a[i][i]  #Reshuffle so that we have only xi on the left side 
        diff=np.linalg.norm(z-x)
        x=np.copy(z) # numpy arrays 
    
    print(x)    
