# 973. K Closest Points to Origin
# Problem: https://leetcode.com/problems/k-closest-points-to-origin/
# Submitted: 2026-09-01 14:13 EDT
# Intuition: Squared distance ranks points without needing a square root.
# Approach: Push every point into a distance min-heap and pop the closest k.
# Complexity: O((n + k) log n) time, O(n + k) space.

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        closest = []
        for x, y in points:
            d = x**2 + y**2
            heapq.heappush(heap, (d, x, y))
        
        for _ in range(k):
            d, x, y = heapq.heappop(heap)
            closest.append([x,y])

        return closest
