#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:52:29 2020

@author: tomasferrer
"""

# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def fn(node, q):
            if node == q:
                return True, [node]
            elif not(node):
                return False, None
            else:
                isleft, lpath = fn(node.left, q)
                if isleft:
                    return True, [node] + lpath
                isright, rpath = fn(node.right, q)
                if isright:
                    return True, [node] + rpath
                return False, None
                
        ppath = fn(root, p)[1]
        qpath = fn(root, q)[1]
        
        for i in range(min(len(ppath), len(qpath))-1,-1,-1):
            if ppath[i] == qpath[i]:
                return ppath[i]
            
