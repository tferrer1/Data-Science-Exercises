#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:32:27 2020

@author: tomasferrer
"""

s = "A man, a plan, a canal: Panama"
# clean = ''
# for char in s.lower():
#     if char in 'qwertyuiopasdfghjklzxcvbnm1234567890':
#         clean += char
# print(clean)

# p = int((len(clean)-1)/2)
# print(p)
# print(len(clean))
# print(clean[:p])
# print(clean[p+1:][::-1])


def isPalindrome(s: str) -> bool:
    clean = ''
    for char in s.lower():
        if char in 'qwertyuiopasdfghjklzxcvbnm1234567890':
            clean += char
    p = int((len(clean)-1)/2)
    if len(clean) % 2 == 0:
        return clean[:p+1] == clean[p+1:][::-1]
    else:
        return clean[:p] == clean[p+1:][::-1]
    
print(isPalindrome('ababa!'))