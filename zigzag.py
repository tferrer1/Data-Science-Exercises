#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:45:38 2020

@author: tomasferrer
"""
'''
P   A   H   N
A P L S I I G
Y   I   R


P     I    N
A   L S  I G
Y A   H R
P     I

'''


'''
number of rows - 2 = substeps, '1 row per column'



'''

def convert(s, nRows):
    
    if nRows == 1:
        print(s)
        return s
    
    zz = []
    for i in range(nRows):
        zz.append([])
    
    curr_row = 0
    downwards = True

    
    for i in range(len(s)):
        
        zz[curr_row].append(s[i])
        
        if curr_row == 0:
            downwards = True
            curr_row += 1
            
        elif curr_row == (nRows-1):
            downwards = False
            
            if i != len(s)-1:
                for j in range(nRows):
                    zz[j].append(" ")
                    
            curr_row -= 1
        
        else:
            if downwards:
                if i != len(s)-1:
                    curr_row += 1
                else:
                    for j in range(curr_row, nRows):
                        zz[j].append(" ")
            else:
                for j in range(nRows):
                    if j != curr_row:
                        zz[j].append(" ")
                curr_row -= 1
                if curr_row == 0:
                    for j in range(nRows):
                        zz[j].append(" ")
    
    print("")    
    printer = []
    for i in range(nRows):
        msg = ''
        for char in zz[i]:
            msg += char 
        printer.append(msg)
    
    for line in printer:
        print(line)
        
    msg = ''
    for row in zz:
        for char in row:
            if char != " ":
                msg += char
    
    
    print("\n"+msg)            
    
    return msg
        
convert("H", 8)
        
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        