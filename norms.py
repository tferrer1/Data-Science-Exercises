#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:08:29 2020

@author: tomasferrer
"""
import numpy as np
import matplotlib.pyplot as plt

qnorm = lambda q, vec: sum([abs(x)**q for x in vec]) ** (1/q)

q = 1

X = np.linspace(-1,1,1001)

y = + (1 - abs(X)**q) ** (1/q)
y2 = -(1 - abs(X)**q) ** (1/q)

plt.plot(X, y)
plt.plot(X, y2)




