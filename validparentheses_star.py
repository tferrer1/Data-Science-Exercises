#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:00:26 2020

@author: tomasferrer

Valid parenthesis
"""

def checkValidString(s):
    n = len(s)
    l = r = 0
    for i in range(n):
        l += 1 if s[i] in '(*' else -1
        r += 1 if s[n-i-1] in ')*' else -1
        if l <0 or r<0: return False
    return True

        
