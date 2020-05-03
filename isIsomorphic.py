#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:24:50 2020

@author: tomasferrer
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        st = {}
        ts = {}
        for i in range(len(s)):
            if s[i] in st.keys() and st[s[i]] != t[i]:
                print("s")
                print(st, s[i], st[s[i]], t[i])
                return False
            if t[i] in ts.keys() and ts[t[i]] != s[i]:
                print("t")
                print(ts, t[i], ts[t[i]], s[i])
                return False
            st[s[i]] = t[i]
            ts[t[i]] = s[i]
        return True


s = "ab"
t = "ca"

print(Solution().isIsomorphic(s,t))