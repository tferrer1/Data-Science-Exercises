#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:06:41 2020

@author: tomasferrer

 Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
 
 Given a binary tree where each path going from the root to any leaf form a valid sequence,
 check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr and the concatenation
of all values of the nodes along a path results in a sequence in the given binary tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr) -> bool: 
        def fn(node, i=0, leaf = False):
            if node:
                if not(i == len(arr)) and node.val == arr[i]:
                    leaf = not(node.left) and not(node.right)
                    left = fn(node.left, i+1, leaf)
                    right= fn(node.right, i+1, leaf)
                    return left or right
                else:
                    return False
            else:
                return i == len(arr) and leaf
        
        return fn(root)
                        
            
"""
check value of root. if == arr[0] continue

check value of root.left. if == arr[1] continue

check value of left.left if == arr[2] dig deeper.

If node is leaf and arr != done, kill the branch, go to the next

"""
# root = TreeNode(8)
# root.left = TreeNode(1)
# root.right = TreeNode(0)
# root.right.left = TreeNode(1)
# root.right.right = TreeNode(1)
# root.right.left.left = TreeNode(1)
# root.right.left.right = TreeNode(0)
# root.right.right.left = TreeNode(1)
# root.right.right.right = TreeNode(0)
# root.right.right.left.left = TreeNode(0)
# root.right.right.left.right = TreeNode(1)

root = TreeNode(8)
# root.left = TreeNode(3)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(1)
# root.left.left.left = TreeNode(5)
# root.left.left.right = TreeNode(4)



arr = [8]

print(Solution().isValidSequence(root, arr))