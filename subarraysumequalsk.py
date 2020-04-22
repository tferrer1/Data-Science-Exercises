#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 10:43:41 2020

@author: tomasferrer

Subarray Sum Equals K

Given an array of integers and an integer k,
 you need to find the total number of continuous
 subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000]
 and the range of the integer k is [-1e7, 1e7].

"""
from collections import defaultdict
def subarraySum(nums, k):
    cnt, cur, ksum = defaultdict(int, {0:1}), 0, 0
    for n in nums:
        cur += n
        ksum += cnt[cur-k]
        cnt[cur] += 1
    return ksum