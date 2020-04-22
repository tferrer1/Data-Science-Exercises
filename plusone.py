#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:22:51 2020

@author: tomasferrer
"""

def plusOne(digits):
    pwr = s = 0
    while digits:
        s += digits.pop()*10**pwr
        pwr += 1
    return  [int(i) for i in str(s+1)]
    
    
    
            
            
            
            
            
            
            
            
            
            
            
            
        
    
    