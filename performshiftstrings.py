#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:07:41 2020

@author: tomasferrer
"""

def shiftString(s, shift):
    l = len(s)    
    for d, m in shift:
        d = (-1) ** d
        s = s[d*(m%l):] + s[:d*(m%l)]
    return s
    
s = "abcdefg"
shift = [[1,1],[1,1],[0,2],[1,3]]

print(shiftString(s,shift))