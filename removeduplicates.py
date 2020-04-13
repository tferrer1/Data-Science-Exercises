#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:49:23 2020

@author: tomasferrer
"""

nums = [1,1,1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,5,6,6,6]
 
 
def removeDuplicates(nums):
    last_val, i, r = None, 0, 0
    while r < len(nums):
        if not(nums[r] == last_val):
            nums[i] = nums[r]
            last_val = nums[i]
            i += 1
        r += 1
    nums[i:] = []
    return len(nums)

print(removeDuplicates(nums))