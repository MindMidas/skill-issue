# 1288. Remove Covered Intervals
# Problem: https://leetcode.com/problems/remove-covered-intervals/
# Submitted: 2026-11-20 13:19 EST
# Intuition: Sorting equal starts by decreasing end puts covering intervals first.
# Approach: Sort by ascending start and descending end, then count intervals
# whose end exceeds the largest end seen so far.
# Complexity: O(n log n) time and O(n) extra space for Python's sort.


class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        max_end = float("-inf")
        remaining = 0

        for start, end in intervals:
            if end > max_end:
                remaining += 1
                max_end = end

        return remaining
