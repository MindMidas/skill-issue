# 162. Find Peak Element
# Problem: https://leetcode.com/problems/find-peak-element/
# Submitted: 2026-11-23 12:16 EST
# Intuition: A peak exists in the direction of an increasing slope.
# Approach: Binary search, returning a midpoint larger than both neighbors.
# Otherwise search left on a downward right slope and right on an upward slope.
# Complexity: O(log n) time and O(1) extra space.


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            ln = nums[mid - 1] if mid - 1 >= 0 else float("-inf")
            rn = nums[mid + 1] if mid + 1 < n else float("-inf")
            if ln < nums[mid] > rn:
                return mid
            if rn < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
