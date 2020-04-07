#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:28:28 2020

@author: tomasferrer
"""


def countElements(arr):
    arr_set = set(arr)
    c = 0
    for x in arr:
        if x+1 in arr_set:
            c += 1
    return c

arr = [1,2,3]

print(countElements(arr))