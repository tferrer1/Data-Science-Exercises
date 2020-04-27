#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:16:20 2020

@author: tomasferrer
"""

class Solution:
    def generate(self, numRows):
        ans = [[1]] if numRows else []
        for _ in range(numRows-1):
            temp = [0] + ans[-1]
            row = []
            for i in range(len(temp)):
                row.append(temp[i]+temp[(i+1)%len(temp)])
            ans.append(row)
        return ans

for row in Solution().generate(10): print(row)
                
                