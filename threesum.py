#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:26:44 2020

@author: tomasferrer


Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

def threeSum(nums):
    nums = sorted(nums)
    
    triplets = set()
    
    checked_ns = set()
    
    for i in range(len(nums)):
        n = nums[i]
        if n in checked_ns:
            continue
        nums_n = nums[:i] + nums[i+1:]
        
        # need a+b s.t. a+b = -n
        # discard impossible numbers
        
        if n < 0:
            sl = [x for x in nums_n if x >= -n - nums_n[-1]]
        else:
            sl = [x for x in nums_n if x <= -n - nums_n[0]]
        
        j = 0
        k = len(sl)-1
        
        while j < k:
            if sl[j] + sl[k] == -n:
                triplets.add(tuple(sorted([sl[j], sl[k], n])))
                j += 1
                k -= 1
            elif sl[j] + sl[k] < -n:
                j += 1
            else:
                k -= 1
        
        checked_ns.add(n)
    
    return [list(trip) for trip in triplets]
        
        
print(threeSum([-1,0,1,2,-1,-4]))