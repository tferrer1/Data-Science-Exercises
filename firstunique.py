#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 07:52:45 2020

@author: tomasferrer

First Unique Number


You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
 

Example 1:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1

Example 2:

Input: 
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output: 
[null,-1,null,null,null,null,null,17]

Explanation: 
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17

Example 3:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output: 
[null,809,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1

 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^8
1 <= value <= 10^8
At most 50000 calls will be made to showFirstUnique and add.

"""

# class FirstUnique:

#     def __init__(self, nums):
#         self.nums = nums
#         self.seen = set()
#         self.firstunique = []
#         self.fuo = dict()
#         for n in nums:
#             if n in self.seen:
#                 p = self.fuo.get(n, False)
#                 if p is not False:
#                     self.firstunique.pop(p)
#                     self.fuo.pop(n)
#                     self.fuo.update(zip(self.firstunique[p:],range(p,len(self.firstunique))))
#             else:
#                 self.seen.add(n)
#                 self.firstunique.append(n)
#                 self.fuo[n] = len(self.firstunique)-1

#     def showFirstUnique(self):
#         return -1 if not self.firstunique else self.firstunique[0]

#     def add(self, value: int):
#         self.nums.append(value)
#         if value in self.seen:
#             p = self.fuo.get(value, False)
#             if p is not False:
#                 self.firstunique.pop(p)
#                 self.fuo.pop(value)
#                 self.fuo.update(zip(self.firstunique[p:],range(p,len(self.firstunique))))
                
#         else:
#             self.seen.add(value)
#             self.firstunique.append(value)
#             self.fuo[value] = len(self.firstunique) -1
        

class FirstUnique:

    def __init__(self, nums):
        self.nums = nums
        self.seen = set()
        self.uniques = []
        self.uniques_set = set()
        for n in nums:
            if n in self.seen:
                if n in self.uniques_set:
                    self.uniques_set.remove(n)
                    self.uniques.pop(self.uniques.index(n))
            else:
                self.seen.add(n)
                self.uniques.append(n)
                self.uniques_set.add(n)

    def showFirstUnique(self):
        return -1 if not self.uniques else self.uniques[0]

    def add(self, value: int):
        self.nums.append(value)
        if value in self.seen:
            if value in self.uniques_set:
                    self.uniques_set.remove(value)
                    self.uniques.pop(self.uniques.index(value))
        else:
            self.seen.add(value)
            self.uniques.append(value)
            self.uniques_set.add(value)
        
        
a = FirstUnique([2,3,5,5,7])

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)