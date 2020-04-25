#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:26:46 2020

@author: tomasferrer


Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root:
            stack = [(root, 1)]
        else:
            return 0
        while stack:
            node, depth = stack.pop(0)
            left = node.left
            if left: stack.append((left, depth+1))
            right = node.right
            if right: stack.append((right, depth+1))
            if not(left) and not(right):
                return depth