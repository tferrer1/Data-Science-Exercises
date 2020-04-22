#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:37:22 2020

@author: tomasferrer

Suppose an array sorted in ascending order is rotated 
at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the 
array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

"""

def search(nums, target):

    s = 0
    e = len(nums)-1
    p = int((s+e)/2)
    
    while e - s > 1:
        if nums[p] == target:
            return p
        elif nums[s] <= nums[p]:
            if nums[s] <= target <= nums[p]:
                e = p
                p = int((s+e)/2)                
            else:
                s = p
                p = int((s+e)/2)
        elif nums[p] <= target <= nums[e]:
            s = p
            p = int((s+e)/2)
        else:
            e = p
            p = int((s+e)/2)
    
    for i, n in enumerate(nums[s:s+2]):
        if n == target:
            return s+i
    return -1
              
# pvt = 29            
# n = 100            
# target = 1

# nums = list(range(n))[-pvt:]+list(range(n))[:n-pvt]
nums = [1,3,5]
target = 5

if target not in nums:
    print(-1, search(nums,target))
else:
    print(target, nums[search(nums,target)])            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
    
    