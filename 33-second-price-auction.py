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
            
        
players = [Bidder("Alice"), Bidder("Bob")]
print("Psst, secret!")
for player in players:
    print("%s's value is %.3f" % (player.name, player.own_val))
auction = Auction(players, verbose=True)
auction.run()



montecarlo = []

n = 100000

for i in range(n):
    r = Auction().run()
    if r > 0.5:
        montecarlo.append(r)
print("\nMean sale price: %.3f" % np.mean(montecarlo))
print("%.2f probability of sale" % (len(montecarlo)/n) )
plt.hist(montecarlo, bins =20)
        
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        