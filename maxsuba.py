#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 19:53:57 2020

@author: tomasferrer
"""

def maxsuba(nums):
    max_sum = -1e999
    pos_max = 0
    for n in nums:
        pos_max += n
        max_sum = max(max_sum, pos_max)
        pos_max = max(0, pos_max)
    return max_sum
            


#nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [-1,-3,-5,7]
#nums = [1,2]
nums = [1,2,-1,-2,2,1,-2,1,4,-5,4]
print(maxsuba(nums))
