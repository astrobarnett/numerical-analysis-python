#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:11:58 2019

@author: astro
"""

x = int(input("Select the type of sorting (1 - Bubble; 2 - Selection; 3 - Quicksort; 4 - Merge): "))
A = [9, -3, 5, 2, 6, 8, -6, 1, 3]
arr = A
# Code for Bubble sort 
if(x==1):
    def bubbleSort(arr):
    	n = len(arr)
    	for i in range(n):
    		for j in range(0, n-i-1): #we'll run loop till (n-i-1) coz first part is sorted and 2 is unsorted
     			if arr[j] > arr[j+1] : #If element at first place is greater than swap 
    			   arr[j],arr[j+1] = arr[j+1],arr[j]
    
    bubbleSort(arr)    
    print (arr)
# Code for selection sort 
if(x==2):
    for i in range(len(A)): 
    	min_idx = i #minimum index number 
    	for j in range(i+1, len(A)): # 
    		if A[min_idx] > A[j]: #condition to check minimum element 
    			min_idx = j   #update the index of minimum element
    	A[i], A[min_idx] = A[min_idx], A[i] 
    
    print (A)  
# Code for Quicksort      
if(x==3):
    def partition(arr,low,high): # array , start (low) and end (high) index of the segment that need to be sorted (becoz we don't want to create any new array) 
    	i = ( low-1 )	#first element which will be 0=start-1   	 
    	pivot = arr[high]# we have chose pivot end index of the segment	  
    
    	for j in range(low , high): #for loop for the array 
    		if arr[j] < pivot: #swap if element is lesser than pivot
    			i = i+1
    			arr[i],arr[j] = arr[j],arr[i]    
    	arr[i+1],arr[high] = arr[high],arr[i+1] 
    	return ( i+1 ) 
    
    def quickSort(arr,low,high): #function for quicksort
    	if low < high: #
    		pi = partition(arr,low,high) #calling partition  
    		quickSort(arr, low, pi-1) #recursive calls to sort the segment left of the partition index (low to till pi-1 ) 
    		quickSort(arr, pi+1, high) #recursive calls to sort the segment right or towards the higher indices of the partition index (pi+1 to till high )
            
    n = len(arr) 
    quickSort(arr,0,n-1) 
    print ("Sorted array is:") 
    for i in range(n): 
    	print ("%d" %arr[i]), 
# Code for Merge sort 
if(x==4):
    def mergeSort(arr): # function for merge sort
    	if len(arr) >1: 
    		mid = len(arr)//2 # Divide the array 
    		L = arr[:mid] #left array till mid  
    		R = arr[mid:] #right array till mid
    
    		mergeSort(L) #recursive calls to merge
    		mergeSort(R) #recursive calls to merge
    
    		i = j = k = 0 # i,j will mark the index of the smallest "unpicked" in L and R respectively while k will mark the index of the position that needs to be filled in array (arr) 
            
    		while i < len(L) and j < len(R): 
    			if L[i] < R[j]: 
    				arr[k] = L[i] 
    				i+=1
    			else: 
    				arr[k] = R[j] 
    				j+=1
    			k+=1
    		
    		while i < len(L): 
    			arr[k] = L[i] 
    			i+=1
    			k+=1
    		
    		while j < len(R): 
    			arr[k] = R[j] 
    			j+=1
    			k+=1
    
    def printList(arr): 
    	for i in range(len(arr)):		 
    		print(arr[i],end=" ") 
    	print() 
    
    if __name__ == '__main__': 
    	print ("Given array is", end="\n") 
    	printList(arr) 
    	mergeSort(arr) 
    	print("Sorted array is: ", end="\n") 
    	printList(arr)
