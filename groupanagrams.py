#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 11:41:49 2020

@author: tomasferrer

each word is a dictionary. letter: occurrences

dictionary : list of words that have this dictionary



"""

def groupAnagrams(strs):
    
    anagrams = dict()
    
    for word in strs:
        x = dict(zip(set(word), [0]*len(word)))
        for char in word:
            x[char] += 1
        
        x = str(sorted((key, value) for (key,value) in x.items()))
        
        if x in anagrams.keys():
            anagrams[x].extend([word])
        else:
            anagrams[x] = [word]
    
    return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))
    