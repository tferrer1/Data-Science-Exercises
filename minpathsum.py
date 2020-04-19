#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:25:30 2020

@author: tomasferrer

Given a m x n grid filled with non-negative numbers,
 find a path from top left to bottom right which minimizes 
 the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
class Solution:
    def minPathSum(self, grid):
        def neighbors(node):
            nb = set()
            i,j = node[0],node[1]
            if i < len(grid)-1:
                nb.add((i+1,j))
            if j < len(grid[0])-1:
                nb.add((i,j+1))
            return nb

        d = dict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                d[(i,j)] = float('inf')
        d[(0,0)] = grid[0][0]

        stack = set([(0,0)])
        while len(stack) > 0:
            s = stack.pop()
            for node in neighbors(s):
                d[node] = min(d[s]+grid[node[0]][node[1]], d[node])
                stack.add(node)        
        return d[(len(grid)-1,len(grid[0])-1)]
    
# grid = [[1,3,1],[1,5,1],[4,2,1]]

# print(Solution().minPathSum(grid))

grid = [[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]]

print(Solution().minPathSum(grid))


