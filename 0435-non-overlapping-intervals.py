# 435. Non-overlapping Intervals
# Problem: https://leetcode.com/problems/non-overlapping-intervals/
# Submitted: 2026-09-02 11:30 EDT
# Intuition: Keeping the earliest-finishing interval leaves maximum room for later ones.
# Approach: Sort by end time and count intervals that overlap the last kept interval.
# Complexity: O(n log n) time, O(n) worst-case space for Python sorting.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])
        minimum = 0
        prev = None

        for interval in intervals:

            if not prev:
                prev = interval
            
            else:

                if interval[0] < prev[1]:
                    minimum += 1
                else:
                    prev = interval
        
        return minimum