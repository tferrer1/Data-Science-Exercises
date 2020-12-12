#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:23:57 2020

@author: tomasferrer
"""

def letterCombinations(digits):
    button = dict(zip('23456789',['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']))
    ans = [] if not(digits) else list(button[digits[0]])
    for n in digits[1:]:
        nxt = []
        for s in ans:
            nxt += [s+x for x in button[n]]
        ans = nxt
    return ans