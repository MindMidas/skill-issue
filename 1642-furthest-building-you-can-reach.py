# 1642. Furthest Building You Can Reach
# Problem: https://leetcode.com/problems/furthest-building-you-can-reach/
# Submitted: 2026-11-25 11:29 EST
# Intuition: Reserve ladders for the largest climbs and spend bricks on smaller climbs.
# Approach: Push positive climbs into a min-heap. When climbs outnumber ladders,
# pay bricks for the smallest climb, stopping when bricks run out.
# Complexity: O(n log(min(n, ladders + 1) + 1)) time and
# O(min(n, ladders + 1)) space.

import heapq


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        min_heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            heapq.heappush(min_heap, diff)
            if len(min_heap) > ladders:
                bricks -= heapq.heappop(min_heap)
            if bricks < 0:
                return i

        return len(heights) - 1
