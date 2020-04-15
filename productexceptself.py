#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:43:53 2020

@author: tomasferrer

Given an array nums of n integers where n > 1,  
return an array output such that output[i] 
is equal to the product of all the elements
 of nums except nums[i].
 
Solve it without division.

"""

def productExceptSelf(nums):
    ans = [1] * len(nums)
    
    left, right = 1, 1
    
    for i in range(len(nums)):
        ans[i] = ans[i] * left
        ans[-1-i] = ans[-1-i] * right
        left = left * nums[i]
        right = right * nums[-1-i]
    
    return ans


print(productExceptSelf([1,2,3,4,5]))
