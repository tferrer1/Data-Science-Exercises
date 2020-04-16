#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:35:50 2020

@author: tomasferrer
"""

def countAndSay(n):
    ans = '1'
    for _ in range(n-1):
        curr_num = ans[0]
        ctr = i = 0
        tmp = ''
        while i < len(ans):
            if ans[i] == curr_num:
                ctr += 1
            else:
                tmp += str(ctr) + str(curr_num)
                curr_num = ans[i]
                ctr = 1
            if i == len(ans) - 1:
                tmp += str(ctr) + str(curr_num)
            i += 1
        ans = tmp
    return ans

n=30
print(countAndSay(n))