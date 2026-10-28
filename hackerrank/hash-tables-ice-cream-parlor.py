#!/bin/python3
# HackerRank - Hash Tables: Ice Cream Parlor
# Intuition: For each flavor, look for an earlier flavor costing money minus its price.
# Approach: Map seen costs to 1-based IDs; check the complement before storing the current flavor.
# Complexity: O(n) average time, O(n) extra space per trip.

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    
    seen = {} # store 1-indexed flavour with cost as key
    
    # iterate over each flavour and cost
    for f, c in enumerate(cost, start=1):
        
        # get target cost to spend all money
        target = money - c
        
        # check if we've seen it, otherwise add
        if target in seen:
            print(f"{seen[target]} {f}")
            return
        
        seen[c] = f
            
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
