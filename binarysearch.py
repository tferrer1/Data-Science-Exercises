#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:34:43 2020

@author: tomasferrer
"""

def binarySearch(nums, target):
    lo, hi = 0, len(nums)    
    while lo < hi:
        mid = (lo+hi) //2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid+1
    return -1 if lo == len(nums) else lo if nums[lo] == target else -1

n = 1000000000
import numpy as np
import timeit

start = timeit.time.perf_counter()
print(binarySearch(list(range(n)),np.random.randint(n)))
print('time:',timeit.time.perf_counter()-start)