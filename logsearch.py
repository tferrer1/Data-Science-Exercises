#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:48:35 2020

@author: tomasferrer
"""

def logsearch(array, e):    
    start = 0
    end = len(array)-1
    
    p = int((start + end)/2)
    last_p = None
    
    while True:
        if array[p] < e:
            if p == len(array)-1:
                return -1
            else:
                start = p
                nxt = max(int((start + end)/2), p+1)
                if last_p == nxt:
                    return p+1 #discard leftover if not needed
                else:
                    last_p = p
                    p = nxt
        elif array[p] > e:
            if p == 0:
                return -1
            else:
                end = p
                nxt = min(int((start + end)/2), p-1)
                if last_p == nxt:
                    return p #discard leftover if not needed
                else:
                    last_p = p
                    p = nxt
        else:
            return p
        
n = 100000000
import numpy as np
import timeit

start = timeit.time.perf_counter()
print(logsearch(list(range(n)),np.random.randint(n)))
print('time:',timeit.time.perf_counter()-start)