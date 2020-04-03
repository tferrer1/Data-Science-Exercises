#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:19:19 2020

@author: tomasferrer
"""

#O(n**2) solution

def maxArea(heights):
    
    max_a = 0
        
    for i in range(len(heights)):
        for j in range(i, len(heights)):
            a = min(heights[i], heights[j]) * (j - i)
            max_a = max(a, max_a)
            
       
    return max_a
        
        
heights = [1,8,4,1,1,1,1,1,1,1,1]

print(maxArea(heights))

#O(n) solution

def maxwater(h):
    i = 0 
    j = len(h)-1
    water = 0
    
    while i < j:
        water = max(water, min(h[i],h[j])*(j-i))
        if h[j] > h[i]:
            i += 1
        else:
            j -= 1
    return water
 

heights = [1,8,4,1,1,1,1,1,1,1,1]

print(maxwater(heights))