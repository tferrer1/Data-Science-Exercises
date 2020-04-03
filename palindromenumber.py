#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:49:02 2020

@author: tomasferrer
"""

def isPalindrome(x):
    
    x = str(x)
    i = 0
    j = len(x) - 1
    
    if j < 1:
        return True    
    else:
        while j - i > 0:
            if x[j] == x[i]:
                i += 1
                j -= 1
            else:
                return False
        return True
    

x = ''

print(isPalindrome(x))
            
    
    