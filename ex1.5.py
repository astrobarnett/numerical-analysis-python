#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:11:40 2019

@author: astro
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm


f1=str('tmerg_bin.dat') 
f2=str('chirpmass_bin.dat')
f3=str('chirpmass_tmerg_tot.dat')
#input the filename as a string

x=np.genfromtxt(f1,comments="#",dtype="float")  
y=np.genfromtxt(f2,comments="#",dtype="float")              
z=np.genfromtxt(f3,comments="#",dtype="float")               

"""
The first argument of genfromtxt is the name of the input file (defined as string)
float is type of variable.
# represent The character used to indicate the start of a comment. 
#All the characters occurring on a line after a comment are discarded  
"""
for i in range(len(y)): #for loop in f2
    for j in range(len(x)): #for loop in f1
        if(z[i,j]<=0.0): # if condition in f3 
            z[i,j]=0.1
        z[i,j]=np.log10(z[i,j])

#set contours
cs=plt.contourf(x, y, z, 30, cmap=cm.Reds) 
"""
# The last letter 'f' stands for 'filled' while plt.contour produces unfilled contour lines 
z: a two dimensional array-like object of size n × m. The values over which the contour is drawn.
x and y represent the coordinates of the values in z. x and y must both be 2D arrays with the same shape as z
cmap: string. Sets the color map. 

"""

# set color bar
cbar=plt.colorbar(cs,orientation='vertical')
#plt.colorbar, which is needed to generate a color bar for the contour plot.
cbar.solids.set_edgecolor("face")

# plot the data
plt.axis([0., 14., 0., 40.])

#ax=plt.gca()
#ax.annotate("5x10**4",xy=(3.75168,3.6962))

plt.xlabel('tmerg [Gyr]', fontsize=10)
plt.ylabel('Mchirp [solar M]', fontsize=10)
plt.show()
