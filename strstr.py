#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:24:31 2020

@author: tomasferrer
"""

def strStr(haystack, needle):
    if not(needle): return 0
    l = len(needle)
    for i in range(len(haystack)):
        if haystack[i:i+l] == needle:
            return i
    return -1