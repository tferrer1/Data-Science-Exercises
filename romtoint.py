#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:01:05 2020

@author: tomasferrer
"""
def romtoint(s):
    m = dict(zip(['I','V','X','L','C','D','M'],[1,5,10,50,100,500,1000]))
    c = 0
    last_digit = 1e100

    for numeral in s:
        number = m[numeral]
        c += number
        if last_digit < number:
            c -= 2*last_digit
        last_digit = number

    return c
        