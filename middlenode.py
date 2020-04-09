#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:37:13 2020

@author: tomasferrer
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""

head

[a, a, a, a, a, a, a, a, a, None]



"""


def middleNode(head):
    
    nodeList = [head]
    nxt = head.next
    
    while nxt != None:
        nodeList.append(nxt)
        nxt = nxt.next
    
    return nodeList[int(len(nodeList)/2)]
    
    
    
    
    