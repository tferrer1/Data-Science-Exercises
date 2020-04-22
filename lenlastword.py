#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:10:21 2020

@author: tomasferrer
"""

def lengthOfLastWord(s):
    
    while s[-1:] == ' ':
        s = s[:-1]
    
    for i, char in enumerate(s[::-1]):
        if char == ' ':
            return i
    return len(s)         