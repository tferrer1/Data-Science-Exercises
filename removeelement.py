#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:37:31 2020

@author: tomasferrer
"""

def removeElement(nums, val):
    i = 0
    r = 0
    l = len(nums)
    while i < l:
        if nums[r] == val:
            del(nums[r])
            r -= 1
        i += 1   
        r += 1
    
    return len(nums)

nums = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums, val))