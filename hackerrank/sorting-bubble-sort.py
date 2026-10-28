#!/bin/python3
# HackerRank - Sorting: Bubble Sort
# Intuition: Swap adjacent out-of-order values until the array is sorted, counting every swap.
# Approach: Run n passes over neighboring pairs, then print the swap count and sorted endpoints.
# Complexity: O(n^2) time even for sorted input, O(1) extra space.

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):

    n = len(a)
    swaps = 0
    
    # bubble sort
    for i in range(n):
        for j in range(n-1):
            # swap if larger
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1 # increment counter
    
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
