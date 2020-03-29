#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 19:02:49 2020

@author: tomasferrer
"""

'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        
        n1 = 0
        i = 0
        
        reader = l1
        
        while True:
            n1 += reader.val * (10 ** i)
            i += 1
            reader = reader.next
            if not(reader):
                break
            
        n2 = 0
        i = 0
        
        reader = l2
        
        while True:
            n2 += reader.val * (10 ** i)
            i += 1
            reader = reader.next
            if not(reader):
                break

        n3 = n1 + n2
                
        lst = []
        first = True
        for digit in reversed(str(n3)):
            print(n3)
            node = ListNode(int(digit))
            if first:
                lst.append(node)
                first = False
                continue
            lst[-1].next = node
            lst.append(node)
        
        return lst[0]
        
    
#lst = [ListNode(1)]
#
#for i in range(29):
#    node = ListNode(0)
#    lst.append(node)
#    lst[i].next = node
#lst[-1].next = ListNode(1)
#
#
#l1 = lst[0]
#
#l2 = ListNode(5)
#l2.next= ListNode(6)
#l2.next.next = ListNode(4)

l1 = ListNode(0)
l2 = ListNode(0)

sol = Solution()
l3 = sol.addTwoNumbers(l1, l2)
       
        