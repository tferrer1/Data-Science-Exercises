#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:17:58 2020

@author: tomasferrer

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""


def merge(nums1, m, nums2, n):   
        i = len(nums1)-1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
                i -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
                i -= 1
        if m < 0:
            nums1[:i+1] = nums2[:n+1]

            
                
import numpy as np
np.random.seed(122451)
nums1 = [x for x in list(range(10)) if np.random.rand() > 0.5]
nums2 = [x for x in list(range(10)) if np.random.rand() > 0.5]
print('nums1',nums1)
print('nums2',nums2)
m = len(nums1)
n = len(nums2)
nums1 += [0] * n
print("merge!")
merge(nums1, m, nums2, n)
print(nums1)