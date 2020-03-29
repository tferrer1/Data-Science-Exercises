#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:43:03 2020

@author: tomasferrer
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 23:01:18 2020

@author: tomasferrer
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:37:43 2020

Different types of players:
    
    - Scumbags: never cooperate
    - Pidgeons: always cooperate
    - Tit for tats: will cooperate. if wronged, will retaliate, but will forgive
    - Grudger: will cooperate. but if wronged, will never cooperate again
    - Hitfirst: will not cooperate at first, but if 

At the end of the game, the 10 players with the least money
die and are replaced by a random sample fron the surviving
cohorts

@author: tomasferrer
"""

from collections import defaultdict
import random
import matplotlib.pyplot as plt
import numpy as np

class Player():
    def __init__(self):
        self.blacklist= defaultdict(bool);
        self.forgiver = True
        self.money = 0;
        self.type = None
        
    def cooperate(self, counterpart):
        return not (self.blacklist[counterpart])
    
    def reset(self):
        self.money = 0
        self.blacklist= defaultdict(bool);
        
class Pidgeon(Player):
    def __init__(self):
        super().__init__()
        self.type = "pidgeon"
    def cooperate(self, counterpart):
        return True
        
class Scumbag(Player):
    def __init__(self):
        super().__init__()
        self.type = "scumbag"
    def cooperate(self, counterpart):
        return False
    
class Grudger(Player):
    def __init__(self):
        super().__init__()
        self.type = "grudger"
        self.forgiver = False

class Tit4tat(Player):
    def __init__(self):
        super().__init__()
        self.type = "tit4tat"
        
class Hitfirst(Player):
    def __init__(self):
        super().__init__()
        self.type = "hitfirst"
        
    def cooperate(self, counterpart):
        if counterpart not in self.blacklist.keys():
            return False
        else:
            return not (self.blacklist[counterpart])

def spawn(s):
    if s == "pidgeon":
        return Pidgeon()
    elif s == "scumbag":
        return Scumbag()
    elif s == "grudger":
        return Grudger()
    elif s =="tit4tat":
        return Tit4tat()
    elif s == "hitfirst":
        return Hitfirst()
    else:
        raise NameError("%s is not a  valid key" % s)

def game(p1, p2):
    if p1.cooperate(p2):
        if p2.cooperate(p1):
            if p1.forgiver:
                p1.blacklist[p2] = False
#            print("both cooperate")
            p1.money += 3
            p2.money += 3
            
        else:
            p2.money += 5
            p1.blacklist[p2] = True
#            print("%s screwed %s" % (p2.name, p1.name))
            
        if p2.forgiver:
            p2.blacklist[p1] = False
            
    elif p2.cooperate(p1):
        p1.money += 5
        p2.blacklist[p1] = True
#        print("%s screwed %s" % (p1.name, p2.name))
        if p1.forgiver:
            p1.blacklist[p2] = False
    else:
        p1.money += 1
        p2.money += 1
        p1.blacklist[p2] = True
        p2.blacklist[p1] = True
#        print("both screwed each other")

census = []

pidgeons = []
hitfirsts = []
grudgers = []
tit4tats = []
scumbags = []

census = [pidgeons, hitfirsts, grudgers, tit4tats, scumbags]
labels = ['pidgeon', 'hitfirst', 'grudger', 'tit4tat', 'scumbag']

# initialize
population = []

init = {'pidgeon': 20,
        'hitfirst':20,
        'grudger':20,
        'tit4tat':20,
        'scumbag':20}

for i in range(init['pidgeon']):
    population.append(Pidgeon())
for i in range(init['hitfirst']):
    population.append(Hitfirst())
for i in range(init['grudger']):
    population.append(Grudger())
for i in range(init['tit4tat']):
    population.append(Tit4tat())
for i in range(init['scumbag']):
    population.append(Scumbag())

def update_census(cns, pop):
    
    counter = dict(zip(labels, [0]*len(labels)))
    
    for i in pop:
        counter[i.type] += 1
    
    mapper = dict(zip(labels, range(len(labels))))
    for t in counter.keys():
        cns[mapper[t]].extend([counter[t]])
        
update_census(census, population)

def pairup(population):
    def pop_random(lst):
        idx = random.randrange(0, len(lst))
        return lst.pop(idx)

    lst = population
    pairs = []

    while lst:
        rand1 = pop_random(lst)
        rand2 = pop_random(lst)
        pair = rand1, rand2
        pairs.append(pair)
    
    return pairs



def randomize_w(dx):
    keys = list(dx.keys())
    weights = dx.values()
    scale= []
    for i, val in enumerate(weights):
        if i == 0:
            scale.append(val)
        else:
            scale.extend([scale[-1]+val])
    
    rand = scale[-1]*np.random.rand()
    ptr = 0
    while True:
        if rand <= scale[ptr]:
            return keys[ptr]
        else:
            ptr += 1

endcensus = []

endpidgeons = []
endhitfirsts = []
endgrudgers = []
endtit4tats = []
endscumbags = []

endcensus = [endpidgeons, endhitfirsts, endgrudgers, endtit4tats, endscumbags]

for universes in range(100):
    for epoch in range(100):
        
        pairs = pairup(population)
               
        wallet = defaultdict(int)   
            
        for x1, x2 in pairs:
            for i in range(10):
                game(x1, x2)
            wallet[x1.type] += x1.money
            wallet[x2.type] += x2.money
    
        for i in range(97):
            population.append(spawn(randomize_w(wallet)))
    #        population.append(spawn('tit4tat'))
        for i in range(3):
            population.append(spawn(random.sample(labels, 1)[0]))
    
        update_census(census, population)
    for i, each in enumerate(endcensus):
        each.append(census[i][-1])        
    
plt.boxplot(endcensus, labels=labels)
