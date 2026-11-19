# 986. Interval List Intersections
# Problem: https://leetcode.com/problems/interval-list-intersections/
# Submitted: 2026-11-19 11:43 EST
# Intuition: Only the current intervals from the two sorted lists can overlap.
# Approach: Record their overlap when present, then advance the interval that ends sooner.
# Complexity: O(m + n) time and O(1) auxiliary space, excluding the output.


class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        i = 0
        j = 0
        intersections = []

        while i < len(firstList) and j < len(secondList):
            i_start, i_end = firstList[i]
            j_start, j_end = secondList[j]
            start = max(i_start, j_start)
            end = min(i_end, j_end)
            if start <= end:
                intersections.append([start, end])

            if i_end <= j_end:
                i += 1
            else:
                j += 1

        return intersections
