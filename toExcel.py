#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:12:18 2020

@author: tomasferrer
"""

# def changebase(x, base =10):
#     slot = []
#     while x > 0:
#         slot = [x%base] + slot
#         x = x //base
#     return slot
    
# print(changebase(15,9))

def toExcel(x, base=27):
    result = []
    while x > 0:
        q = x // base
        r = x % base + q
        while r // base > 0:
            q += r // base
            r = r % base + r // base     
        result = [r] + result
        x = q
    dd = dict(zip(range(1,27),'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    return ''.join([dd[x] for x in result])

print(toExcel(1001))