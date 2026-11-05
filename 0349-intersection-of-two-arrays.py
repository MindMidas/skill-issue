# 349. Intersection of Two Arrays
# Problem: https://leetcode.com/problems/intersection-of-two-arrays/
# Submitted: 2026-11-05 15:01 EST
# Intuition: Each shared value should appear only once, so use sets.
# Approach: Intersect the two sets with & and convert the result to a list.
# Complexity: O(n + m) expected time and O(n + m) extra space for the sets.

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        return list(set(nums1) & set(nums2))
