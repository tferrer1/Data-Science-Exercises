#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:58:13 2020

@author: tomasferrer
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(n1, n2):
            if n1 and n2:
                if n1.val == n2.val:
                    left = check(n1.left, n2.left)
                    right = check(n1.right, n2.right)
                    return left & right
                else:
                    return False
            elif n1 == n2 == None:
                return True
            else:
                return False
        return check(p,q)
    