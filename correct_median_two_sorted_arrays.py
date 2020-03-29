#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:31:12 2020

@author: tomasferrer
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        
        if len(nums2)<len(nums1):
            nums1,nums2=nums2,nums1
            
        l1=len(nums1)
        l2=len(nums2)
        start,end=0,l1
        c = 0
        while True:
            
            p1= (start+end)//2
            p2=((l1+l2+1)//2)-p1
            
            print("turn %i" % c)
            print("p1",p1)
            print("p2",p2)
            c += 1
            
            p1max= -1e500 if p1==0 else nums1[p1-1]
            p1min=1e500 if p1>=l1 else nums1[p1]
            
            p2max= -1e500 if p2==0 else nums2[p2-1]
            p2min= 1e500 if p2>=l2 else nums2[p2]
            
            if p1max<=p2min and p2max<=p1min:
                if (l1+l2)%2:
                    return max(p1max,p2max)
                else:
                    return (max(p1max,p2max)+min(p1min,p2min))/2
            elif p1max>p2min:
                end=p1-1
            else:
                start=p1+1
                print("hippy")
                
                
   
import timeit
nums1 = list(range(1,50))
nums2 = list(range(50,100))

if 1:
    starttime = timeit.default_timer()  
            
    print("algo's solution: ", Solution().findMedianSortedArrays(nums1, nums2))
    
    log_time = timeit.default_timer() - starttime
    print("Log search, Time to complete : %.6f seconds" % (log_time))


#import numpy as np

#starttime = timeit.default_timer()

#print("correct:", np.median(nums1 + nums2))

#linear_time = timeit.default_timer() - starttime
#print("Linear search, Time to complete : %.6f seconds" % (linear_time))

#print("log was ",int(linear_time / log_time), " times faster")

    
        