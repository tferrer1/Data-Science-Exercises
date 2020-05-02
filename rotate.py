#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:09:14 2020

@author: tomasferrer
"""
# class Solution:
#     def rotate(self, nums, k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k %= len(nums)
#         a = nums[-k:]
#         b = nums[:len(nums)-k]
#         print(a, b)
#         nums[:k-1] = a
#         nums[k:] = b

# nums = [1,2,3,4,5,6,7]
# k = 29

# Solution().rotate(nums, k)
# print(nums)

class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:k-1], nums[k:] = nums[-k:], nums[:len(nums)-k]

nums = [1,2,3,4,5,6,7]
k = 1

Solution().rotate(nums, k)
print(nums)