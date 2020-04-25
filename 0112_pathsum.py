#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:01:24 2020

@author: tomasferrer
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        stack = []
        if root:
            stack.append((root, root.val))
        while stack:
            node, s = stack.pop(0)
            left = node.left
            if left: stack.append((left, s + left.val))
            right = node.right
            if right: stack.append((right, s + right.val))
            if not(left) and not(right):
                if s == sum: return True
        return False
        