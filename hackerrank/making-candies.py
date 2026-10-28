#!/bin/python3
# HackerRank - Making Candies
# Intuition: Balanced machine and worker counts maximize production, but saving instead of buying may finish sooner.
# Approach: Track the best finish without more upgrades, skip to the next affordable purchase, and balance bulk upgrades.
# Complexity: O(b) time, O(1) extra space; b is the number of purchase or fast-forward batches.

import math
import os
import random
import re
import sys

#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#

def minimumPasses(m, w, p, n):
    
    # goal : minimize number of passes to obtain required number of candies at the end of a day. Determine that number of passes.
    
    # m * w -> yields candies produced
    # p -> cost to buy m/w
    
    best = (n + m * w - 1) // (m * w) # worst case

    passes = 0
    candies = 0
    
    while passes < best:
        
        # base case: we reached target
        if candies >= n:
            return passes
        
        # produce candies if we haven't reached target and can't buy
        if candies < n and candies < p:
            new_passes = (p - candies + m * w - 1) // (m * w)
            if passes + new_passes >= best:
                return best
            passes += new_passes
            candies += m*w*new_passes
            continue
        
        # we could buy or not
        # calc new best if we stop buying 
        best = min(best, passes + (n - candies + m * w - 1) // (m * w))
        # calc total possible upgrades and diff between m and w
        upgrades = candies // p
        diff = abs(m - w)
        min_upgrades = min(diff, upgrades)
        
        # add upgrades to smaller side to make them as equal
        if m < w:
            m += min_upgrades
        elif w < m:
            w += min_upgrades
        
        # calc and assign leftover evenly
        leftover = upgrades - min_upgrades
        if leftover > 0:
            side = leftover // 2
            remainder = leftover % 2
            m += side + remainder
            w += side
        
        # update candies and passes after buying
        candies -= upgrades * p
        candies += m*w
        passes += 1
    
    return best
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
