#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:11:40 2019

@author: astro
"""

import numpy as np
fname=fname=str('illustris3_135.dat')
IDs=np.genfromtxt(fname, dtype="float",usecols=(0)) 
#sorting algorithm
def quicksort(arr): 
    c=[]
    d=[]
    m=[]

    if(len(arr)>1):
        p=arr[0] #pivot chosen & print(p)
        for x in arr:
            if(x>p):
                c.append(x)  #array of elements after the pivot 
            elif(x<p):
                d.append(x) #array of elements before the pivot
            elif(x==p):
                m.append(x) #array with the pivot
        return quicksort(d) + m + quicksort(c)
    else:
        return arr
print(quicksort(IDs))
