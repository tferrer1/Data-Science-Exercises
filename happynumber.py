#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 19:34:35 2020

@author: tomasferrer
"""

def isHappy(n):
    
    noughts = {n}
    
    while True:
        
        s = 0
        for d in str(n):
            s += int(d) ** 2
            
        if s == 1:
            return True
        elif s in noughts:
            return False
        else:
            noughts.add(s)
            n = s            
