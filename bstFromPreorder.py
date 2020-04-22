#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:43:47 2020

@author: tomasferrer

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant
 of node.left has a value < node.val, and any descendant of node.right has a value > node.val. 
 Also recall that a preorder traversal displays the value of the node first, then traverses
 node.left, then traverses node.right.)

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:          
        def getNodes(node, j, maxval):
            if not(j >= len(preorder)) and preorder[j] < node.val:
                node.left, j = getNodes(TreeNode(preorder[j]),j+1, node.val)
            if not(j >= len(preorder)) and node.val < preorder[j] < maxval : 
                node.right, j = getNodes(TreeNode(preorder[j]),j+1,maxval)
            return node, j
        return getNodes(TreeNode(preorder[0]), 1, float("Inf"))[0]
            
preorder = [8,5,1,7,10,12]

a = Solution().bstFromPreorder(preorder)