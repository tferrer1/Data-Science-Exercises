#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:20:48 2020

@author: tomasferrer
"""

#loongest substring in a string w/o repeating characters

#chr chr chr chr chr chr chr chr chr chr chr chr chr

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        
        max_len = 0
                
        for i in range(len(s)):
            if s[i] not in substring:
                substring += s[i]
                if len(substring) > max_len:
                    max_len = len(substring)
            else:
                substring += s[i]
                substring = substring[substring.index(s[i])+1:]
                    
        return max_len

print(Solution().lengthOfLongestSubstring("dvdf"))
