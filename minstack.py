#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:30:28 2020

@author: tomasferrer

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_pos = []
        self.min = 1e9999
    
    def push(self, x):
        self.stack.append(x)
        if x < self.min:
            self.min = x
            self.min_pos.append(len(self.stack)-1)
            
    def pop(self):
        if len(self.stack) == 0:
            pass
        else:
            self.stack = self.stack[:-1]
            if len(self.stack) == self.min_pos[-1]:
                self.min_pos = self.min_pos[:-1]
                if len(self.stack) > 0:
                    self.min = self.stack[self.min_pos[-1]] 
                else:
                    self.min = 1e999
    
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
        
    def getMin(self):
        if len(self.stack) > 0:
            return self.min
        else:
            return None
        
        
minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print(minStack.getMin());
minStack.pop();
print(minStack.top());
print(minStack.getMin());










