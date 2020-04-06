#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:42:11 2020

@author: tomasferrer
"""

def moveZeros(nums):
    size = len(nums)
    i, ctr = 0, 0
    while ctr < size:
        if nums[i] == 0:
            nums.append(nums.pop(i))
            i -= 1
        ctr += 1
        i += 1
    
    return nums
