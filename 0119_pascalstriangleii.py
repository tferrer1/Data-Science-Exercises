#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:55:46 2020

@author: tomasferrer

119. Pascal's Triangle II

"""

class Solution:
    def getRow(self, rowIndex):
        ans = [1]   
        for _ in range(rowIndex):
            ans = [0] + ans
            temp = []
            for i in range(len(ans)):
                temp.append(ans[i]+ans[(i+1)%len(ans)])
            ans = temp
        return ans
        