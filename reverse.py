#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:42:24 2020

@author: tomasferrer
"""

def reverse(x):
    
    sign = (-1, 1)[x > 0]
        
    rst = sign * int(str(abs(x))[::-1])
    
    return rst if -2**31 <= rst < 2 **31 else 0 
        

num = -123

print(reverse(num))