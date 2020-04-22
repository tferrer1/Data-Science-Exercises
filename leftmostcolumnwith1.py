#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:18:24 2020

@author: tomasferrer
"""

import numpy as np

class BinaryMatrix(object):
    def __init__(self, matrix = None, n=100):
        self.matrix = matrix or [sorted(np.random.randint(0,2,n)) for _ in range(n)]
        self.dims = len(self.matrix), len(self.matrix[0])
    def get(self, x,y):
        return self.matrix[x][y]
    def dimensions(self):
        return self.dims
    def print_matrix(self):
        for row in self.matrix:
            print(row)
    def check_ans(self, ans):
        return sum([x[ans-1] for x in self.matrix]) == 0 and sum([x[ans] for x in self.matrix]) > 0

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix):
        binaryMatrix.print_matrix()
        n,m = binaryMatrix.dimensions()
        lm = float("inf")
        for row in range(n):
            # print("working with", binaryMatrix.matrix[row])
            s, e, lc = 0, m-1, None
            col = min(lm-1, int((s+e)/2))
            while True:
                val = binaryMatrix.get(row, col)
                # print("checked", row, col, "=", val)
                if val:
                    e = lm = col
                    # print("lm updated to", lm)
                    if lm == 0: return 0
                    col = min(int((s+e)/2),col-1)
                    if col == lc: break
                    lc = col
                else:
                    if lm == col+1: break
                    s = col
                    col = max(int((s+e)/2),col+1)
                    if col == lc or col == m: break
                    lc = col
        return lm if lm < m else -1

matrix = BinaryMatrix(n=50)
matrix.print_matrix()
ans = Solution().leftMostColumnWithOne(matrix)
print(ans, matrix.check_ans(ans))
            