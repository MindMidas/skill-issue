# 605. Can Place Flowers
# Problem: https://leetcode.com/problems/can-place-flowers/
# Submitted: 2026-10-29 12:32 EDT
# Intuition: Planting in the earliest available safe plot leaves as much room as possible for later flowers.
# Approach: Scan left to right, plant where the plot and its neighbors are empty, and decrease the remaining count.
# Complexity: O(m) time, O(1) extra space; m is the flowerbed length. The flowerbed is modified in place.

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        for i,_ in enumerate(flowerbed):
            
            # All requested flowers have been planted.
            if n == 0:
                return True
            
            # Plant only if this plot and both existing neighbors are empty.
            if ( flowerbed[i] == 0 and
                 (i == 0 or flowerbed[i-1] == 0) and 
                 (i == len(flowerbed)-1 or flowerbed[i+1] == 0) ):
                
                flowerbed[i] = 1
                n -= 1

        return n == 0
