# 846. Hand of Straights
# Problem: https://leetcode.com/problems/hand-of-straights/
# Submitted: 2026-09-03 14:29 EDT
# Intuition: The smallest remaining card must begin the next consecutive group.
# Approach: Use frequencies and a min-heap, consume a straight, then reinsert remaining copies.
# Complexity: O(n log n) time, O(n) space.

import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        freq = {}
        heap = []

        for card in hand:
            if card not in freq:
                freq[card] = 1
                heapq.heappush(heap, card)
            else:
                freq[card] += 1
        
        
        while heap:
            
            straight = []
 
            for i in range(groupSize):
                
                if heap:
                    smallest = heapq.heappop(heap)
                else:
                    return False
                
                if i == 0:
                    straight.append(smallest)
                elif (straight[i-1] + 1) != smallest:
                    return False
                else: 
                    straight.append(smallest)
 
            for card in straight:
                freq[card] -= 1
                if freq[card] >= 1:
                    heapq.heappush(heap, card)

        return True
