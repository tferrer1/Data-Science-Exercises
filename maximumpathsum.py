#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:43:41 2020

@author: tomasferrer
"""

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#O(n^2) solution
        
# class Solution:
#     def maxPathSum(self, root: TreeNode) -> int:
#         path = {}
#         parents = {}
#         def navigate(node):
#             path[(node, node)] = node.val
#             print("set path for node", node.val)
#             if node.left:
#                 parents[node.left] = node
#                 path[(node, node.left)] = path[(node.left, node)] = node.val + node.left.val
#                 print("set path between",node.val,"and",node.left.val,"to", node.val + node.left.val)
#                 navigate(node.left)
#             if node.right:
#                 parents[node.right] = node
#                 path[(node, node.right)] = path[(node.right, node)] = node.val + node.right.val
#                 print("set path between",node.val,"and",node.right.val,"to", node.val + node.right.val)
#                 navigate(node.right)
        
#         navigate(root)
#         print("done navigating")
             
#         parental_line = {}
        
#         def get_ascendancy(x):
#             ascendants = []
#             node = x
#             while node in parents.keys():
#                 ascendants.append(parents[node])
#                 node = parents[node]
#             return ascendants
        
#         for x in [root] + list(parents.keys()):
#             parental_line[x] = get_ascendancy(x)
        
#         print("done parenting")
        
#         def get_path(x, y):
#             print("checking path between",x.val,"and",y.val)
#             if (x,y) not in path.keys():
#                 print("(",x.val,",",y.val,") not in keys")
#                 if not x in parental_line[y]:
#                     path[(x,y)] = path[(y,x)] = x.val + get_path(parents[x],y)
#                     print("path between",x.val,"and",y.val,"set to",path[(x,y)],"!")
#                 else:
#                     path[(x,y)] = path[(y,x)] = y.val + get_path(parents[y],x)
#                     print("path between",x.val,"and",y.val,"set to",path[(x,y)],"!")
#             return path[(x,y)]
        
        
#         for node_i in [root]+list(parents.keys()):
#             for node_j in [root]+list(parents.keys()):
#                 get_path(node_i, node_j)
            
#         return max(path.values())
    
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:   
        global maxvalue
        maxvalue = float("-inf")
        
        def maxPathDown(node):
            global maxvalue
            if not(node): return 0
            left = max(0, maxPathDown(node.left))
            right = max(0, maxPathDown(node.right))
            maxvalue = max(maxvalue, left + right + node.val)
            return max(left, right) + node.val
        
        maxPathDown(root)
        
        return maxvalue
    
        

root = TreeNode(1)

root.left = TreeNode(2)

root.right = TreeNode(3)

# root.left.left = TreeNode(3)

# root.left.left.left = TreeNode(4)

# root.left.left.left.left = TreeNode(5)


print(Solution().maxPathSum(root))