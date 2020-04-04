#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:54:15 2020

@author: tomasferrer
"""


def int_to_rom(x):
    
    x = str(x)[::-1]
    
    uni = ('I', 'V', 'X')
    dec = ('X', 'L', 'C')
    cen = ('C', 'D', 'M')
    mil = ('M', None, None)
    
    units = [uni, dec, cen, mil]
    
    lista = []
    
    i = 0
    
    while i < len(x):   
        atom, half, nxt = units[i]

        n = int(x[i])
        rom_n = ''
        
        if n == 0:
            rom_n = ''        
        elif n < 4:
            rom_n = n * atom
        elif n == 4:
            rom_n = atom + half
        elif n < 9:
            rom_n = half + atom * (n-5)
        else:
            rom_n = atom + nxt
        
        lista.append(rom_n)
        i += 1
        
    lista = lista[::-1]
    
    return "".join(lista)
    


        
        