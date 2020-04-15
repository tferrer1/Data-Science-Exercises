#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:14:02 2020

@author: tomasferrer
"""

def isBadVersion(n):
    bad = 5
    return n >= bad

def firstBadVersion(n):
    start = 1
    end = n 
    p = int((end+start)/2)   
    while True:
        if isBadVersion(p):
            if p == 1:
                return p
            else:
                end = p
                p = int((start+end)/2)
        else:
            if p+1 == end:
                return p+1
            else:
                start = p
                p = int((start+end)/2)
            
print(firstBadVersion(5))