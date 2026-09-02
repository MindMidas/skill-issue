# 56. Merge Intervals
# Problem: https://leetcode.com/problems/merge-intervals/
# Submitted: 2026-09-02 10:54 EDT
# Intuition: After sorting, overlaps can only extend the most recent merged interval.
# Approach: Sort intervals and either extend the last result or start a new interval.
# Complexity: O(n log n) time, O(n) space including output and sorting.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        merged = []

        for interval in intervals:

            if not merged:
                merged.append(interval)
            else:
                
                prev = merged[-1]

                if prev[1] >= interval[0]:
                    prev[1] = max(prev[1], interval[1])
                else:
                    merged.append(interval)

        return merged
