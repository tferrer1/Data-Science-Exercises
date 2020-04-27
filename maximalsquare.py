#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:00:35 2020

@author: tomasferrer
 
Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 1 1 1

1 1 1 1 1
1 2 2 1 1
1 2 3 1 1
0 1 2 1 1



Output: 4

"""

def maximalSquare(matrix):
    if not(matrix) or not(matrix[0]): return 0
    matrix = [[int(i) for i in row] for row in matrix]
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j] > 0:
                matrix[i][j] = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j])+1
    return max([i for j in matrix for i in j])**2
