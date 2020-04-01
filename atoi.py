#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:07:25 2020

@author: tomasferrer
"""

'''

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary
 until the first non-whitespace character is found. Then, starting from this character, 
 takes an optional initial plus or minus sign followed by as many numerical digits as 
 possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number,
 which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, 
or if no such sequence exists because either str is empty or it contains only whitespace 
characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the
 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the
 range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
 
 '''
 
def atoi(string):
    def isnum(z):
        if z in '1234567890':
            return True
        else:
            return False
    
    if len(string) == 0:
        return 0
    
    i = 0
    
    while i < len(string):
        if string[i] == ' ':
            i += 1
        else:
            break
        if i == len(string):
            return 0
    
    some_number = False
    
    num = ''
    if string[i] in '+-':
        num += string[i]
        i += 1
    
    while i < len(string):
        if isnum(string[i]):
            num += string[i]
            some_number = True
            i += 1
#            print(num)
        else:
            if string[i] == ".":
                if "." not in num:
                    num += string[i]
                    i += 1
                    continue
                else:
                    return 0
            
            if some_number:
                break
            else:
                return 0
    
    try:   
        num = int(float(num))
    
    except:
        return 0    
        
    num = min(max(-2**31, int(num)), 2**31-1)
    
    
    return num
        
    
s = "  -0012a42"

print(atoi(s))
    
        