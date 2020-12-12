#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:50:28 2020

@author: tomasferrer
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        def fn(node):
            if node:
                c, xnode = fn(node.next)
                
                node.next = xnode
                
                if c == n:
                    node = node.next
                
                return c+1, node
            else:
                return 1, node
        
        return None if not(head.next) else fn(head)[1]
    
    
head = ListNode(2)
head.next = ListNode(4)

print(Solution().removeNthFromEnd(head,2).val)
    