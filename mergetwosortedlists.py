#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:44:28 2020

@author: tomasferrer
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:       
        lst = []      
        while (l1 != None) or (l2 != None):
            v1 = 1e999 if not l1 else l1.val
            v2 = 1e999 if not l2 else l2.val
                        
            if v2 <= v1:
                lst.append(v2)
                l2 = l2.next
            else:
                lst.append(v1)
                l1 = l1.next

        node, sol = None, None
        for val in lst[::-1]:
            sol = ListNode(val)
            sol.next = node
            node = sol

        return sol
   
node = ListNode(4)
nod = ListNode(2)
nod.next = node
l1 = ListNode(1)
l1.next = nod


node = ListNode(4)
nod = ListNode(3)
nod.next = node
l2 = ListNode(1)
l2.next = nod

print(Solution().mergeTwoLists(l1,l2))