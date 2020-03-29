#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:37:43 2020

Different types of players:
    
    - Scumbags: never cooperate
    - Pidgeons: always cooperate
    - Tit for tats: cooperate if the other person cooperates

At the end of the game, the 10 players with the least money
die and are replaced by a random sample fron the surviving
cohorts

@author: tomasferrer
"""

import numpy as np
from collections import defaultdict

class Player():
    def __init__(self, name):
        self.name = name
        self.blacklist= defaultdict(bool);
        self.forgiver = True
        self.money = 0;
        self.type = None
        
    def cooperate(self, counterpart):
        return not (self.blacklist[counterpart])
        
class Pidgeon(Player):
    def __init__(self, name):
        super().__init__(name)
        self.type = "pidgeon"
    def cooperate(self, counterpart):
        return True
        
class Scumbag(Player):
    def __init__(self, name):
        super().__init__(name)
        self.type = "scumbag"
    def cooperate(self, counterpart):
        return False
    
class Grudger(Player):
    def __init__(self, name):
        super().__init__(name)
        self.type = "grudger"
        self.forgiver = False

class Tit4tat(Player):
    def __init__(self, name):
        super().__init__(name)
        self.type = "tit4tat"
        
class Hitfirst(Player):
    def __init__(self, name):
        super().__init__(name)
        self.type = "hitfirst"
        
    def cooperate(self, counterpart):
        if counterpart not in self.blacklist.keys():
            return False
        else:
            return not (self.blacklist[counterpart])

def game(p1, p2):
    if p1.cooperate(p2):
        if p2.cooperate(p1):
            if p1.forgiver:
                p1.blacklist[p2] = False
            print("both cooperate")
            p1.money += 3
            p2.money += 3
            
        else:
            p2.money += 5
            p1.blacklist[p2] = True
            print("%s screwed %s" % (p2.name, p1.name))
            
        if p2.forgiver:
            p2.blacklist[p1] = False
            
    elif p2.cooperate(p1):
        p1.money += 5
        p2.blacklist[p1] = True
        print("%s screwed %s" % (p1.name, p2.name))
        if p1.forgiver:
            p1.blacklist[p2] = False
    else:
        p1.money += 1
        p2.money += 1
        p1.blacklist[p2] = True
        p2.blacklist[p1] = True
        print("both screwed each other")

tom = Tit4tat("Tom")

paul = Pidgeon("Paul")

steve = Scumbag("Steve")

gary = Grudger("Gary")
    
harry = Hitfirst("Harry")
