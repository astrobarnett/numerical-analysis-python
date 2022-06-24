#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:25:58 2019

@author: astro
"""

import os #This module provides a portable way of using operating system dependent functionality 
         #it is needed to call re

import re  # regular expression module 
import matplotlib.pyplot as plt

rh = re.compile('^  kira_rhalf = (\d+.\d+)')# the string I want to look for: half-mass radius rh
#The ’+’ symbol after ’d’ indicates that I am searching only strings where 
#there is AT LEAST ONE integer digit in that position of the
#string (but there might be many more).

t = re.compile('^  t  =  (\d+.\d+)') # the string I want to look for: time  
# ^ means that the string should be at the start of a row


f=open(str('starlab_output.txt')) ##input the filename as a string

col1=[] # half-mass radius rh list 
col2=[] # time list 
tempo=0.0

for s in f: #s is a generic string in f
    time = t.search(s) # I search for string t in s
    if(time!=None): 
        tempo=eval(time.group(1)) # group all the value of time it finds    
    rhalf = rh.search(s) # I search for string rh in s
    if(rhalf!=None):
        col2.append(eval(rhalf.group(1))) # group all the value of rhalf it finds
        col1.append(tempo)

#the eval function evaluates the “String” like a python expression and returns the result as an integer.


# To plot    
plt.plot(col1, col2) 
plt.axis([0., 219., 0.5, 2.]) #axis labeling 
plt.xlabel('time (code units)', fontsize=20)
plt.ylabel('half-mass radius (pc)', fontsize=20)
plt.show()
