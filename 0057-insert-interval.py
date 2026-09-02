# 57. Insert Interval
# Problem: https://leetcode.com/problems/insert-interval/
# Submitted: 2026-09-01 20:50 EDT
# Intuition: Only intervals touching the new interval need merging.
# Approach: Binary-search its position, merge overlaps forward, and concatenate untouched slices.
# Complexity: O(n) time, O(n) space including returned slices.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        left = 0
        right = len(intervals)

        while left < right:
            mid = (left + right) // 2 
            # left chunk 
            if newInterval[0] > intervals[mid][0]:
                left = mid + 1
            # right chunk
            else:
                right = mid
            
        
        if left > 0 and intervals[left - 1][1] >= newInterval[0]:
            left -= 1
            newInterval[0] = min(newInterval[0], intervals[left][0])
            newInterval[1] = max(newInterval[1], intervals[left][1])
        
        right = left

        while right < len(intervals) and intervals[right][0] <= newInterval[1]:
            newInterval[0]= min(newInterval[0], intervals[right][0])
            newInterval[1]= max(newInterval[1], intervals[right][1])
            right += 1

        return intervals[:left] + [newInterval] + intervals[right:]
