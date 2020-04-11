#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:10:11 2020

@author: tomasferrer
"""

def longestCommonPrefix(strs):
    
    if len(strs) == 0:
        return ''
    
    prefix = ''
    i = 0
    
    while i < min([len(s) for s in strs]):
        if  [s[i] for s in strs] == [strs[0][i]]*len(strs):
            prefix += strs[0][i]
            i += 1
        else:
            break

    return "".join(prefix)
    
