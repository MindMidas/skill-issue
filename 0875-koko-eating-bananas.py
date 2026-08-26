# 875. Koko Eating Bananas
# Problem: https://leetcode.com/problems/koko-eating-bananas/
# Submitted: 2026-08-26 15:00 EDT
# Intuition: If an eating speed is sufficient, every larger speed is sufficient too.
# Approach: Binary-search the minimum speed, summing rounded-up hours for all piles.
# Complexity: O(n log M) time, O(1) space; M is the largest pile.

import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        answer = 0

        while left <= right:

            mid = left + (right - left) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours <= h:
                right = mid - 1
                answer = mid
            else:
                left = mid + 1
        
        return answer
        
