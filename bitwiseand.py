#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:30:44 2020

@author: tomasferrer
"""

def rangeBitwiseAnd(m,n):
    # if m == n:
    #     return m
    m=bin(m)[2:]
    n=bin(n)[2:]
    pwr = max(len(m),len(n))     
    m = '0'*(pwr-len(m))+m
    n = '0'*(pwr-len(n))+n
    s= 0    
    for i in range(pwr):
        if m[i] != n[i]:
            break
        elif m[i] =='1':
            s += 2**(pwr-1)
        pwr-=1
    return s

print(rangeBitwiseAnd(0,0))
















