#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:11:40 2019

@author: astro
"""
import numpy as np

#Ax=b
A = np.array([[4., -1., 1.], [-1., 4., -2.], [1., -2., 4.]]) #array a
b = np.array([[12.], [-1.], [5.]]) #array b


x = np.zeros((len(A), 1), float) #transform A into an array x 
z = np.zeros((len(A), 1), float)#transform b into an array z
diff= 100.

    
while(diff>1e-8):
    for i in range(len(b)): #for loop in b 
        c = 0.0  # initial value for the diagonal term
        for j in range(len(b)): 
            if (j != i): #if col(j) not equal to row(i) 
                 c += A[i][j]*x[j]  # Extract the diagonal terms from the sum  
        z[i] = (b[i]-c)/A[i][i] # Reshuffle so that we have only xi on the left side
    diff=np.linalg.norm(z-x)
    x=np.copy(z) # numpy arrays 

print(x)    
