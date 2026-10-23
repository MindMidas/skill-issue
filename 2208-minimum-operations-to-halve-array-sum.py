# 2208. Minimum Operations to Halve Array Sum
# Problem: https://leetcode.com/problems/minimum-operations-to-halve-array-sum/
# Submitted: 2026-10-23 15:00 EDT
# Intuition: Halving the largest number gives the biggest reduction toward half the original sum.
# Approach: Use a max-heap via negated values; halve and reinsert the largest until the sum reaches the target.
# Complexity: O(n + k log n) time, O(n) space; k <= n, so O(n log n) worst-case time.

import heapq

class Solution:
    def halveArray(self, nums: list[int]) -> int:
       
        total = sum(nums)
        half = total/2
        total_ops = 0

        heap = [-n for n in nums]
        heapq.heapify(heap)

        while total > half:
            n = heapq.heappop(heap)
            n = n/2
            total += n
            heapq.heappush(heap, n)
            total_ops += 1
        
        return total_ops