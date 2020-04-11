#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:13:49 2020

@author: tomasferrer

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def depth(root):
            if not root: return 0
            left = depth(root.left)
            right = depth(root.right)
            self.ans = max(self.ans, left + right) # path
            return max(left, right) + 1 # depth
        depth(root)
        return self.ans


