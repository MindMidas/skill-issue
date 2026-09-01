# 703. Kth Largest Element in a Stream
# Problem: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Submitted: 2026-09-01 12:45 EDT
# Intuition: Keeping the largest k values makes the heap minimum the kth largest.
# Approach: Heapify the supplied list, trim it to k, and trim again after each add.
# Complexity: O(n log(n+1)) initialization, O(log(k+1)) add; O(k) retained heap, O(1) extra space.

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)