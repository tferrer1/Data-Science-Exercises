#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 18:12:53 2020

@author: tomasferrer
"""
def maxProfit(prices):
        mx = 0
        maxes = [mx]
        for p in prices[::-1]:
            if p > mx:
                maxes = [p] + maxes
                mx = p
            else:
                maxes = [mx] + maxes    
        profits = [0]
        for i in range(len(prices)-1):
            profits.append(maxes[i]-prices[i])
        return max(profits)
    
prices = list(range(10000,0,-1))
prices = [9,9,9,9,5]
print(maxProfit(prices))