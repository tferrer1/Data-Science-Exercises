#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:24:55 2020

@author: tomasferrer
"""

def backspaceCompare(S,T):
    
    String = []
    
    for  char in S:
        if char == "#":
            String = String[:-1]
        else:
            String.append(char)
    
    Ttring = []
    for  char in T:
        if char == "#":
            Ttring = Ttring[:-1]
        else:
            Ttring.append(char) 
    
    return String == Ttring


S = "ab#c"
T = "ad#c"

S = "ab##"
T = "c#d#"
 

S = "a##c"
T = "#a#c"

S = " "
T = "#### "

print(backspaceCompare(S,T))