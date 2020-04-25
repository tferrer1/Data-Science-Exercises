#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 14:13:05 2020

@author: tomasferrer

108. Convert Sorted Array to Binary Search Tree
Easy

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def fn(array):
            if len(array) == 0:
                return None
            elif len(array) == 1:
                return TreeNode(array[0])
            else:
                m = int((len(array)+ (-1 if len(array) % 2 else 0))/2)
                left, root, right = array[:m], array[m], array[m+1:]
                root = TreeNode(root)
                root.left = fn(left)
                root.right = fn(right)
                return root
        return fn(nums)
    
"""
get array

root = median

split into two branches

[] x []

again, select median (always CEILING)
divide into two arrays


if len(array) is 1, done (TreeNode(val))
is len(array) us 0, done (none)

"""

