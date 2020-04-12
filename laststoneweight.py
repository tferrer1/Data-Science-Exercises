#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:38:57 2020

@author: tomasferrer

LAST STONE WEIGHT

We have a collection of stones,
 each stone has a positive integer weight.

Each turn, we choose the two heaviest stones
 and smash them together.  
 
 Suppose the stones  have weights x and y with x <= y. 
 The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, 
    and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left. 
 Return the weight of this stone (or 0 if there are 
                                  no stones left.)

1 <= stones.length <= 30
1 <= stones[i] <= 1000

"""

def lastStoneWeight(stones):
    
    stones = sorted(stones)
    
    def binaryInsert(array, e):   
        if len(array) ==0:
            return [e]
        
        start = 0
        end = len(array)-1
        
        p = int((start + end)/2)
        last_p = None
        
        while True:
            if array[p] <= e:
                if p == len(array)-1:
                    return (array + [e])
                else:
                    start = p
                    nxt = max(int((start + end)/2), p+1)
                    if last_p == nxt:
                        return (array[:p+1] + [e] + array[p+1:]) #discard leftover if not needed
                    else:
                        last_p = p
                        p = nxt
            elif array[p] > e:
                if p == 0:
                    return ([e] + array)
                else:
                    end = p
                    nxt = min(int((start + end)/2), p-1)
                    if last_p == nxt:
                        return (array[:p] + [e] + array[p:]) #discard leftover if not needed
                    else:
                        last_p = p
                        p = nxt
    
    while len(stones) >= 2:
        y = stones.pop()
        x = stones.pop()   
        
        # print("We combine %i and %i to get %i" % (x,y,y-x))

        if x != y:
            stones = binaryInsert(stones, y-x)
            
        # print("... so the array converts to ", stones)
        
    return 0 if len(stones) == 0 else stones[0]
    
    
stones = [316,157,73,106,771,828,46,212,926,604,600,992,71,51,477,869,425,405,859,924,45,187,283,590,303,66,508,982,464,398]

print(lastStoneWeight(stones))
            
            
            
            
            
            
            
            