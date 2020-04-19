#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:20:33 2020

@author: tomasferrer
"""

def numIslands(grid):
    
    checked = set()
    
    def neighbors(i,j,grid):
        neigh = set()
        if i > 0:
            neigh.add((i-1,j))
        if j > 0:
            neigh.add((i,j-1))
        if i < len(grid)-1:
            neigh.add((i+1,j))
        if j < len(grid[0])-1:
            neigh.add((i,j+1))
        return neigh
    
    islands = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if (i,j) in checked:
                continue
            else:
                checked.add((i,j))
                if grid[i][j] == '1':
                    islands += 1
                    stack = []
                    stack.extend(neighbors(i,j,grid)-checked)
                    while len(stack) > 0:
                        r,c = stack.pop()
                        if (r,c) in checked:
                            continue
                        else:
                            checked.add((r,c))
                            if grid[r][c] == '1':
                                stack.extend(neighbors(r,c,grid)-checked)
    return islands

# grid = [[1,1,0,0,0],[1,1,0,0,0,],[0,0,1,0,0],[0,0,0,1,1]]
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(numIslands(grid))           