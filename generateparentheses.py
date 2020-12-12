#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:04:50 2020

@author: tomasferrer
"""

class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        stack = {('',0,n)}
        while stack:
            s, o, r = stack.pop()
            if len(s) == n*2:
                ans.append(s)
            else:
                if o:
                    stack.add((s+')',o-1,r))
                if r:
                    stack.add((s+'(',o+1, r-1))
        return ans

for line in Solution().generateParenthesis(3): print(line)