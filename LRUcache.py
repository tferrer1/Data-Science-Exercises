#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:00:55 2020

@author: tomasferrer
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.lastused = []
        self.positions = {}
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        val = self.cache.get(key,-1)
        if val != -1:
            p = self.positions[key] 
            self.lastused = self.lastused[:p] + self.lastused[p+1:] + [key]
            self.positions = dict(zip(self.lastused, range(len(self.lastused))))
        return val
        
    def put(self, key: int, value: int) -> None:
        val = self.cache.get(key, -1)
        if val != -1:
            self.cache[key] = value
            p = self.positions[key] 
            self.lastused = self.lastused[:p] + self.lastused[p+1:] + [key]
            self.positions = dict(zip(self.lastused, range(len(self.lastused))))
            
        else:
            if len(self.cache) == self.capacity:
                least = self.lastused.pop(0)
                self.cache.pop(least)
            self.cache[key] = value
            self.lastused.append(key)
            self.positions = dict(zip(self.lastused, range(len(self.lastused)))) 

                


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
        
        
