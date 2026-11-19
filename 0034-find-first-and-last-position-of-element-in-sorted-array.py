# 34. Find First and Last Position of Element in Sorted Array
# Problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Submitted: 2026-11-18 19:21 EST
# Intuition: Two binary searches locate the boundaries of a target's occurrences.
# Approach: Find the first index at or after the target and the first index
# after it. Equal indices mean it is absent, otherwise return the inclusive bounds.
# Complexity: O(log(n + 1)) time and O(1) extra space.

from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]
