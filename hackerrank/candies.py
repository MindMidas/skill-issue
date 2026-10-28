#!/bin/python3
# HackerRank - Candies
# Intuition: Every child starts with one candy; higher-rated neighbors impose requirements from both sides.
# Approach: Enforce the left neighbor's requirement going forward, then the right neighbor's going backward, keeping the larger count.
# Complexity: O(n) time, O(n) extra space.

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
        
    # so find min candies to buy
    # each child gets atleast 1
    # if child has higher rating then neighbors, child gets extra candy 
    
    candies = [1] * n
    
    # left to right pass
    for i, score in enumerate(arr):
        l_child = i - 1
        # 1st child doesn't have left neighbour 
        if l_child >= 0:
            
            # update candies since greater then left child
            if score > arr[l_child]:
                candies[i] = candies[l_child] + 1
    
    # right to left pass
    for j in range(n-1, -1, -1):
        score = arr[j]
        r_child = j + 1
        
        # 1st child doesn't have right neighbour 
        if r_child < n:
            
            # take max of curr score and new_score since greater than right child
            if score > arr[r_child]:
                candies[j] = max(candies[j], candies[r_child] + 1)
    
    return sum(candies)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
