#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:03:52 2020

@author: tomasferrer
"""

def climbStairs(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a