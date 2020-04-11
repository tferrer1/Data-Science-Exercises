#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:42:13 2020

@author: tomasferrer
"""


def isValid(s):
    open_ = []
    closure = dict(zip(['[','(','{'], [']',')','}']))
    
    for char in s:
        if char == ' ':
            continue
        elif char in closure.keys():
            open_.append(char)
        else:
            if len(open_) == 0 or char != closure[open_[-1]]:
                return False
            else:
                open_.pop()
            
    return len(open_) == 0             


Input = "()"
print(isValid(Input))

Input = "()[]{}"
print(isValid(Input))

Input = "(]"
print(isValid(Input))

Input = "([)]"
print(isValid(Input))

Input = "{[]}"
print(isValid(Input))