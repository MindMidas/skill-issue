# 1046. Last Stone Weight
# Problem: https://leetcode.com/problems/last-stone-weight/
# Submitted: 2026-09-01 13:40 EDT
# Intuition: Each smash only needs the two heaviest remaining stones.
# Approach: Use negative weights as a max-heap, popping two stones and reinserting their difference.
# Complexity: O(n log n) time, O(n) space.

import heapq

class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        
        while len(heap) > 1:

            y = heapq.heappop(heap)
            x = heapq.heappop(heap)

            if x == y:
                continue
            
            if x != y:
                heapq.heappush(heap, -((-y) - (-x)))
            
        if len(heap) == 0:
            return 0
        else:
            return -heapq.heappop(heap)
