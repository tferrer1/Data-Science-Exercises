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

#for i in range(99):
#    population.append(Pidgeon())
#for i in range(90):
#    population.append(Hitfirst())
for i in range(99):
    population.append(Grudger())
for i in range(1):
    population.append(Tit4tat())
#for i in range(20):
#    population.append(Scumbag())

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

for epoch in range(100):
    
    pairs = pairup(population)
    
    players = []
    scores = []    
        
    for x1, x2 in pairs:
        for i in range(10):
            game(x1, x2)
        players.extend([x1.type, x2.type])
        scores.extend([x1.money, x2.money])
        
    def determine_survivors(plyrs, scores):
        zipped_pairs = zip(scores, plyrs)
        z = [plyr for _, plyr in sorted(zipped_pairs, reverse=True)]
        return z[:int(len(plyrs)*0.9)]
    
    survivors = determine_survivors(players, scores)
    survivors.extend(random.sample(survivors, 9))
    
    for i in range(1):
        population.append(spawn(random.sample(labels, 1)[0]))    
    

    for each in survivors:
        population.append(spawn(each))

    update_census(census, population)


for i, pop in enumerate(census):
    plt.plot(pop, label = labels[i])
    
plt.legend(loc="upper left")
plt.show()

'''
bird : 400
cat : 100
shark: 100
human: 10000

human
bird
cat
shark

'''