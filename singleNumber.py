#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 19:28:13 2020

@author: tomasferrer
"""

def singleNumber(nums):
    
    once = set()
    multiple = set()
    
    for n in nums:
        if n not in once:
            once.add(n)
        else:
            multiple.add(n)
    
    return (once - multiple).pop()

#nums = [2,2,1]
nums = [4,1,2,1,2]
#nums = [0,1]

print(singleNumber(nums))
        