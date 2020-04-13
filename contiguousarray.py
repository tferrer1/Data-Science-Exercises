#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:00:33 2020

@author: tomasferrer
"""
def findMaxLength(nums):
    map_ = {0:-1}
    max_len = 0
    count = 0
    
    for i in range(len(nums)):
        count += 1 if nums[i] else -1
        if count in map_.keys():
            max_len = max(max_len, i - map_[count])
        else:
            map_[count] = i
    return max_len
    


# nums = [1,0,0,0,1,1,0,1,0,1,0,1,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,0,1]
# nums = [0,1,1,0,1,1,1,1,1,0]
# nums = [0,0,1,0,0,1,1,1,0,1,1,0,0,1,0,1,1,1,0,1,1,0,1,0,1]
# nums = [0,1,0,0,0,1,1,0,1,1]
# nums = [0,1,1,1,1,1,1,0] 
# nums = [0,1,1,0,1,1,1,0]
nums = [0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]
print(findMaxLength(nums))