#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 11:45:29 2020

@author: tomasferrer
"""

"""
Suppose you're running a second-price auction.
In this auction, the highest bidder will win,
but will pay the auctioneer (you) the value of
 the second-highest bid.
 
 Assuming there are two bidders bidding on one item,
 and the bidder knows his own valuation but sees the
 valuation of the rival as uncertain and distributed
 uniformly in the unit interval, calculate the 
 expected revenue when the reserve price is 1/2.

"""
import numpy as np
import matplotlib.pyplot as plt

class Auction():
    def __init__(self, players=None, verbose=False):
        ## If no input, initialize with two players
        if players == None:
            self.players = [Bidder(), Bidder()] 
        else:
            self.players = players
        self.current_price = 0.5
        self.second_price = 0.5
        self.current_winner = None
        self.player_checked = dict(zip(self.players, [False] * len(self.players)))
        self.verbose = verbose
        
    def take_bid(self, bidder, bid):
        if self.verbose:
            print("%s offers %.3f!" % (bidder.name, bid))
        self.current_winner = bidder.name
        self.second_price = self.current_price
        self.current_price = bid
        self.player_checked = dict(zip(self.players, [False] * len(self.players)))
        self.player_checked[bidder] = True
        
    def run(self):
        if self.verbose:
            print("......................\n(.... Drumrolls! ....)\n......................")
            print("Price starts at %.3f!" % (self.current_price))
        while sum(self.player_checked.values()) < len(self.players):
            for player in self.players:
                if not self.player_checked[player]:
                    player.assess(self)
                    self.player_checked[player] = True
        if self.verbose:
            if self.current_winner != None:
                print("...")
                print("1, 2, 3... Sold to %s, for %.3f!" % (self.current_winner, self.second_price))
            else:
                print("...")
                print("Auction deserted! :-(")
        if self.current_winner != None:
            return(self.second_price)
        else:
            return(-1)
        
class Bidder():
    def __init__(self, name=None, own_val=-1):
        if own_val < 0:
            self.own_val = np.random.rand()
        else:
            self.own_val = own_val
        
        if name == None:
            self.name = str(self.own_val)
        else:
            self.name = name
            
    def make_bid(self, Auction, bid):
        Auction.take_bid(self, bid)

    def assess(self, Auction):
        if(Auction.current_price < self.own_val):
            self.make_bid(Auction, Auction.current_price + 0.1*(self.own_val - Auction.current_price))
        else:
            pass
            
        
#players = [Bidder("Alice"), Bidder("Bob")]
#print("Psst, secret!")
#for player in players:
#    print("%s's value is %.3f" % (player.name, player.own_val))
#auction = Auction(players, verbose=True)
#auction.run()



montecarlo = []

n = 100000

for i in range(n):
    r = Auction().run()
    if r > 0.5:
        montecarlo.append(r)
print("\nMean sale price: %.3f" % np.mean(montecarlo))
print("%.2f probability of sale" % (len(montecarlo)/n) )
plt.hist(montecarlo, bins =20)


        
"""
25% N N -- No sale
25% N Y -- Sale, 0.50
25% Y N -- Sale, 0.50
25% Y Y -- Sale... for what value?

if you win, you pay the price you beat.
don't shoot yourself in the foot.
Just beat it by the minimum.

So you won't pay to beat a price that's already above
your own value.


def fn(x):
    return min(np.random.rand(), np.random.rand())
    
distribution --> skewed!

not uniform anymore, but triangle

1 --> overwritten by every other value, hence, 0 prob.
0.9 --> overwritten by 80% of values.
0.5 --> Never overwritten (max chance)

probability?

Expect value of this distribution?

int(x * (1-x)) / int(1-x) between 0 and 1

1/3 of the way between 0 and 1

***

prices settled... problem? step-ups

why is there a spike in 0.50?

reserve price: 0.50

player A 0.8

player B 0.51 (or very close to 50)

A's first step will surpass B's own value. So A will pay 0.50, not .51

***

"""
        
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        