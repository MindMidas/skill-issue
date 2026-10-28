#!/bin/python3
# HackerRank - 2D Array - DS
# Intuition: Each hourglass is fixed by its top-left cell; check all 16 possible positions.
# Approach: Sum the seven cells at each position and keep the largest sum, including negative sums.
# Complexity: O(1) time and extra space for the fixed 6-by-6 grid.

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
        
    max_sum = None
    
    # iterate over rows and cols 
    # leftmost cell of hourglass gives start, so (3,3) is highest
    for r in range(4):
        for c in range(4):
            # calculate current sum
            curr_sum = (arr[r][c] + arr[r][c+1] + arr[r][c+2]
                                  + arr[r+1][c+1] +
                        arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2])
            
            # set max_sum if None or greater
            if max_sum is None:
                max_sum = curr_sum
            max_sum = max(max_sum, curr_sum)
    
    return max_sum
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
