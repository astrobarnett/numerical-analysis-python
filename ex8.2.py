#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 15:11:48 2019

@author: astro
"""
import numpy as np
import math as mt
import matplotlib.pyplot as plt

G=1
m1=m2=1
tin=0
tf=300
h=0.01
N=int((tf-tin)/h)
#x01=[1.0,1.0] initial conditions of particle 1: x01=[x1,y1]
#x02=[-1.0,-1.0] initial condition of particle 2: x02=[x2,y2]
#v01=[-0.5,0.0] initial velocity of particle 1: v01=[vx1,vy1]
#v02=[0.5,0.0] initial velocity of particle 2: v02=[vx2,vy2]
x1=[]
x1.append(1.0)
y1=[]
y1.append(1.0)
x2=[]
x2.append(-1.0)
y2=[]
y2.append(-1.0)
vx1=-0.5 #initial velocity of particle 1
vy1=0.0
vx2=0.5 #initial velocity of particle 2
vy2=0.0

def ax(x1,x2,y1,y2):
    ax=-G*m1*(x1-x2)/(((x1-x2)**2+(y1-y2)**2)**1.5) #eqn for x
    return ax

def ay(x1,x2,y1,y2):
    ay=-G*m1*(y1-y2)/(((x1-x2)**2+(y1-y2)**2)**1.5) #eqn for y 
    return ay



#Euler method 
for i in range(N):
    Ax=ax(x1[i],x2[i],y1[i],y2[i])
    Ay=ay(x1[i],x2[i],y1[i],y2[i])
#equation 140 for position x1 and y1
    X1=x1[i]+vx1*h #eqn 140 for x1
    Y1=y1[i]+vy1*h #eqn 140 for y1
#equation 140 for x2 and y2
    X2=x2[i]+vx2*h #eqn 140 for x2
    Y2=y2[i]+vy2*h #eqn 140 for x2
#store elements for array  
    x1.append(X1)
    y1.append(Y1) 
    x2.append(X2)
    y2.append(Y2)
#equation 140 for velocity x1 and y1
    vx1=vx1+Ax*h #eqn 140 for vx1 
    vy1=vy1+Ay*h #eqn 140 for vy1 
    vx2=vx2-Ax*h #eqn 140 for vx2 
    vy2=vy2-Ay*h #eqn 140 for vy2 
   
    
                        
#plot
g1x,=plt.plot(x1,y1,color='b') #Euler method
plt.plot(x2,y2,color='b') 
plt.xlabel('x',fontsize=20)
plt.ylabel('y',fontsize=20)
plt.tight_layout()
plt.show()


