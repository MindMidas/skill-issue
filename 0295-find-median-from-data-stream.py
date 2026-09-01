# 295. Find Median from Data Stream
# Problem: https://leetcode.com/problems/find-median-from-data-stream/
# Submitted: 2026-09-01 19:59 EDT
# Intuition: The median lies between a lower max-heap and an upper min-heap.
# Approach: Insert into the appropriate heap and rebalance their sizes after each addition.
# Complexity: O(log n) addNum, O(1) findMedian; O(n) space.

import heapq

class MedianFinder:

    def __init__(self):
        self.left = [] # max
        self.right = [] # min 

    def addNum(self, num: int) -> None:
        
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        
        if len(self.right) > len(self.left) + 1: 
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:

        if len(self.left) > len(self.right):
            return -self.left[0]
        
        if len(self.left) < len(self.right):
            return self.right[0]

        return (-self.left[0] + self.right[0]) / 2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()