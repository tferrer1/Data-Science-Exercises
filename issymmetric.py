#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:33:55 2020

@author: tomasferrer
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root):    
    def traverse(root, path):
        lft = rght = root
        i = 0
        while i < len(path):
            if path[i] == '1':
                lft = None if not(lft) else lft.right
                rght = None if not(rght) else rght.left
            else:
                lft = None if not(lft) else lft.left
                rght = None if not(rght) else rght.right
            i += 1
        return lft, rght
    
    seeds = ['0']
        
    while seeds:
        # print(seeds)
        path = seeds.pop(0)
        left, right = traverse(root,path)
        # print('path',path, None if not(left) else left.val, None if not(right) else right.val)
        if not(left) and not(right):
            pass
        elif not(left) or not(right):
            return False
        elif left.val == right.val:
                seeds.append(path+'0')
                seeds.append(path+'1')
        else:
            return False
    
    return True

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetric(root))
    

"""

class Solution:
  def isSymmetric(self, root):
    if root is None:
      return True
    else:
      return self.isMirror(root.left, root.right)

  def isMirror(self, left, right):
    if left is None and right is None:
      return True
    if left is None or right is None:
      return False

    if left.val == right.val:
      outPair = self.isMirror(left.left, right.right)
      inPiar = self.isMirror(left.right, right.left)
      return outPair and inPiar
    else:
      return False
      
"""


