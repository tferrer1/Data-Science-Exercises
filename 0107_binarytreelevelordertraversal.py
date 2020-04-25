#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:43:25 2020

@author: tomasferrer
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        t = self.fn(root)
        return [t[x] for x in range(len(t),0,-1)]
        
    def fn(self, node, d=0, t={}):
        if node:
            d += 1
            t[d] = t.get(d,[]) + [node.val]
            t = self.fn(node.left, d, t)
            t = self.fn(node.right, d, t)
        return t
        
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(3)
root = None

print(Solution().levelOrderBottom(root))