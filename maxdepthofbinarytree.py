#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:27:19 2020

@author: tomasferrer

104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int: 
        def fn(node, d=0, md=0):
            if node:
                d += 1
                md = max(md, d)
                md = fn(node.left, d, md)
                md = fn(node.right, d, md)
            return md
        md = fn(root)     
        return md
    
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(3)
root.right.right.right.right = TreeNode(3)
root.right.right.right.right.left = TreeNode(3)

print(Solution().maxDepth(root))