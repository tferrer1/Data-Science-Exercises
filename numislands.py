#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:46:01 2020

@author: tomasferrer
Given a 2d grid map of '1's (land) and '0's (water),
 count the number of islands. An island is surrounded by water 
 and is formed by connecting adjacent lands horizontally or 
 vertically. You may assume all four edges of the grid are 
 all surrounded by water.
"""

def numIslands(grid):
    dd = {}
    island_count = 0
    my_map = [[0]*len(grid[0])]*len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) in dd.keys(): # if parcel was already marked
                pass # do nothing
            # else, parcel not marked.
            elif grid[i][j] == 1:
                print("original check at",i,j)
                island_count += 1
                dd[(i,j)] = island_count
                # start a pursuit
                stack = []
                if j != len(grid[0])-1:
                    stack.append((i,j+1))
                if i != len(grid)-1:
                    stack.append((i+1,j))
                while len(stack) > 0: # while there are dead ends left
                    print(stack)
                    ci, cj = stack.pop()
                    if (ci,cj) in dd.keys():
                        pass
                    else:
                        if grid[ci][cj]:
                            dd[(ci,cj)] = island_count
                            if cj != len(grid[0])-1:
                                if (ci,cj+1) not in dd.keys():
                                    stack.append((ci,cj+1))
                            if ci != len(grid)-1:
                                if (ci+1,cj) not in dd.keys():
                                    stack.append((ci+1,cj))           
                        else:
                            dd[(ci,cj)] = 0
            else:
                print("original check at",i,j)
                dd[(i,j)] = 0
    print(dd)
    # for i,j in dd.keys():
    #     my_map[i][j] = dd[(i,j)]
    # for row in my_map:
    #     print(row)
    return island_count
    
    # for i,j in dd.keys():
    #     my_map[i][j] = dd[(i,j)]
    # for row in my_map:
    #     print(row)
    # return island_count

grid = [[1,1,1],[1,0,1],[0,1,1]]
print(numIslands(grid))             
                