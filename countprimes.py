#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:48:15 2020

@author: tomasferrer

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
from timeit import timeit



def countPrimes(n):
    nums = range(2,n)
    
    deleted = set()
    primes = []
    c = 0
    for num in nums:
        if num not in deleted:
            c += 1
            primes.append(num)
            for x in range(1, int(n/num)+1):
                deleted.add(x*num)
    print(primes[10000])
    return c
    
print(countPrimes(1000000))    