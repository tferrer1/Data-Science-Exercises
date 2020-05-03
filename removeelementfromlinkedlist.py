#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:48:13 2020

@author: tomasferrer
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node, prev = head, None
        while node:
            if node.val == val:
                if prev: prev.next = node.next
                else: head = node.next
            else: prev = node
            node = node.next
        return head
    
head = ListNode(6, ListNode(6, ListNode(3)))
head = None
val = 6

print(Solution().removeElements(head, val).val)