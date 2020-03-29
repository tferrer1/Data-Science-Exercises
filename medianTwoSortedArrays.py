#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:33:19 2020

@author: tomasferrer
"""

"""

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
      
        def logsearch(array, e):    
            start = 0
            end = len(array)-1
            
            p = int((start + end)/2)
            last_p = None
            
            while True:
                if array[p] <= e:
                    if p == len(array)-1:
                        return (array, [])
                    else:
                        start = p
                        nxt = max(int((start + end)/2), p+1)
                        if last_p == nxt:
                            return (array[:p+1], array[p+1:]) #discard leftover if not needed
                        else:
                            last_p = p
                            p = nxt
                elif array[p] > e:
                    if p == 0:
                        return ([], array)
                    else:
                        end = p
                        nxt = min(int((start + end)/2), p-1)
                        if last_p == nxt:
                            return (array[:p], array[p:]) #discard leftover if not needed
                        else:
                            last_p = p
                            p = nxt
        
        def median(array):
            if len(array) % 2 == 0:
                median = (array[int(len(array)/2)-1] + array[int(len(array)/2)]) /2
            else:
                median = array[int(len(array)/2)]
                
            return median, int((len(array)-1)/2 + 1)
               
        m_plus_n = len(nums1) + len(nums2)
        even = m_plus_n % 2 == 0
        
        target_loc = int((m_plus_n - 1)/ 2) # if even, look for the next value and average. # how many numbers before the median
        
        pre = []
        post = []
        
        a = nums1
        b = nums2
        
        if b[0] >= a[-1]:
            ab = a + b
            if even:
                return (ab[target_loc]+ab[target_loc+1])/2.0
            else:
                return ab[target_loc]
        elif a[0] >= b[-1]:
            ba = b + a
            if even:
                return (ba[target_loc]+ba[target_loc+1])/2.0
            else:
                return ba[target_loc]
            
            
            
        
        if a[0] < b[0] :
            pre, a = logsearch(a,b[0])
        elif a[0] > b[0]:
            pre, b = logsearch(b,a[0])
        
        if b[-1] < a[-1]:
            a, post = logsearch(a, b[-1])
        elif a[-1] < b[-1]:
            b, post = logsearch(b,a[-1])
            
        if len(post) > target_loc:
            if even:
                x1 = post[len(post)-1-target_loc]
                if len(post)-1 == target_loc:
                    x2 = max(a[-1],b[-1])
                else:
                    x2 = post[len(post)-1-target_loc-1]
                return (x1+x2)/2.0
            else:
                return post[len(post)-1-target_loc]
        elif len(pre) > target_loc:
            if even:
                x1 = pre[target_loc]
                if len(pre) -1 == target_loc:
                    x2 = min(a[0], b[0])
                else:
                    x2 = pre[target_loc+1]
                return (x1+x2)/2.0
            else:
                return pre[target_loc]
        
        ptr= len(pre)
        
        while True:
            print(a)
            print(b)
            
            if len(a) <= 2:
                for elem in a:
                    x, y = logsearch(b, elem)
                    b = x + [elem] + y
                if even:
                    return (b[target_loc - ptr] + b[target_loc - ptr + 1])/2.0
                else:
                    return b[target_loc - ptr]
                
            elif len(b) <= 2:
                for elem in b:
                    x, y = logsearch(a, elem)
                    a = x + [elem] + y
                if even:
                    return (a[target_loc - ptr] + a[target_loc - ptr + 1])/2.0
                else:
                    return a[target_loc - ptr]
            
            
            ma, pa = median(a)
            mb, pb = median(b)
            
            b_ma_l, _ = logsearch(b,ma)
            a_mb_l, _ = logsearch(a,mb)
            
            ra = ptr + pa + len(b_ma_l)
            rb=  ptr + pb + len(a_mb_l)
            
            if ra >= target_loc:
                # get rid of values *above* ma
                a, _ = logsearch(a, ma)
                b, _ = logsearch(b, ma)
            else:
                # get rid of values *below* ma
                anms, a = logsearch(a, ma)
                bnms, b = logsearch(b, ma)
                # update len of pre
                ptr += len(anms) + len(bnms)
                
            
            if rb >= target_loc:
                a, _ = logsearch(a, mb)
                b, _ = logsearch(b, mb)
            else:
                # get rid of values *below* ma
                anms, a = logsearch(a, mb)
                bnms, b = logsearch(b, mb)
                # update len of pre
                ptr += len(anms) + len(bnms)
            
        return median

import timeit

nums1 = [1,2, 3,5,6,7,8,9,10,11,12,13,14,15,16,17]
nums2 = [1,2, 20, 24, 29,]      
#
#nums1 = list(range(20,150))
#nums2 = list(range(40,180))

if 1:
    starttime = timeit.default_timer()  
            
    print("algo's solution: ", Solution().findMedianSortedArrays(nums1, nums2))
    
    log_time = timeit.default_timer() - starttime
    print("Log search, Time to complete : %.6f seconds" % (log_time))


import numpy as np

starttime = timeit.default_timer()

print("correct:", np.median(nums1 + nums2))

linear_time = timeit.default_timer() - starttime
print("Linear search, Time to complete : %.6f seconds" % (linear_time))

print("log was ",int(linear_time / log_time), " times faster")

