#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:32:02 2020

@author: tomasferrer
"""

# def searchInsert(nums, target):
    
#     start = 0
#     end = len(nums)-1
    
#     p = int((start+end)/2)
    
#     while True:
#         # print(p)
#         if nums[p] == target:
#             return p
#         elif nums[p] > target:
#             if p == 0:
#                 return 0
#             else:
#                 if end == p+1:
#                     return p
#                 else:
#                     end = p
#                     p = min(int((start+end)/2),p-1)    
#         else:
#             if p == len(nums)-1:
#                 return len(nums)
#             else:
#                 if start == p:
#                     return p+1
#                 else:
#                     start = p
#                     p = max(int((start+end)/2),p+1) 

def searchInsert(nums, target):
    if not(nums): return 0    
    start = 0
    end = len(nums)-1
    
    p = int((start + end)/2)
    last_p = None
    
    while True:
        if nums[p] == target:
            return p
        elif nums[p] < target:
            if p == len(nums)-1:
                return len(nums)
            else:
                start = p
                nxt = max(int((start + end)/2), p+1)
                if last_p == nxt:
                    return p+1  
                else:
                    last_p = p
                    p = nxt
        elif nums[p] > target:
            if p == 0:
                return 0
            else:
                end = p
                nxt = min(int((start + end)/2), p-1)
                if last_p == nxt:
                    return p
                else:
                    last_p = p
                    p = nxt
  
# tgt = 17.1
# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

# print(tgt, "is greater than ",nums[searchInsert(nums,tgt)-1])
                  
# print("but smaller or equal to",nums[searchInsert(nums,tgt)])

