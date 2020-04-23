#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:54:58 2020

@author: tomasferrer
"""
import numpy as np

rlist = sorted(np.random.randint(0,5,50))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
    
def ln2list(ln):
    l = []
    while ln:
        l.append(ln.val)
        ln = ln.next
    return l

def list2ln(lst):
    parent = None
    for x in lst[::-1]:
        child = parent
        parent = ListNode(x)
        parent.next = child
    return parent

sol = Solution()
print(rlist)
print(ln2list(sol.deleteDuplicates(list2ln(rlist))))