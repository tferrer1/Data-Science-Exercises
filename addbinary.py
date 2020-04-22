#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:19:17 2020

@author: tomasferrer
"""

def addBinary(a,b):
    s1 = pwr = 0
    for digit in a[::-1]:
        s1 += int(digit)*2**pwr
        pwr += 1
    s2 = pwr = 0
    for digit in b[::-1]:
        s2 += int(digit)*2**pwr
        pwr += 1 
    return bin(s1+s2)[2:]