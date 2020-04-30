#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:58:28 2020

@author: tomasferrer
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head:
            visited = {head}
            node = head
        else:
            return False
        while node.next:
            if node.next in visited:
                return True
            visited.add(node.next)
            node = node.next
        return False
            