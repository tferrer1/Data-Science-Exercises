#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:50:45 2020

@author: tomasferrer


    do i have stock?
    if yes:
        do i sell?
        if price tomorrow is lower than today:
            sell
        else:
            wait
    if no:
        do i buy?
        if price tomorrow is higher than today:
            buy
        else:
            wait

"""

def maxProfit(prices):
    
    # buy only if it goes up at some point
    # buy and sell at the top
    # day is top if p(day + 1) < p(day)
    # day is dip if p(day +1) > p(day)
    # buy dip, sell top
    
    stock_held = 0
    profit = 0
    
    for i in range(len(prices)-1):
        
        if not(stock_held):
            if prices[i+1] > prices[i]:
                stock_held = 1
                cost_basis = prices[i]
        else:
            if prices[i+1] < prices[i]:
                stock_held = 0
                profit += prices[i]-cost_basis
        
    if stock_held:
        profit += prices[-1]-cost_basis
        
    return profit

prices = [2,2,5,9,8]

print(maxProfit(prices))

