# 215. Kth Largest Element in an Array
# Problem: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Submitted: 2026-09-01 14:18 EDT
# Intuition: The kth largest value appears after removing the largest k-1 values.
# Approach: Negate values into a max-heap and pop k times.
# Complexity: O(n + k log n) time, O(n) space.

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        for _ in range(k-1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)
