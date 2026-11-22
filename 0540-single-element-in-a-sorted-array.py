# 540. Single Element in a Sorted Array
# Problem: https://leetcode.com/problems/single-element-in-a-sorted-array/
# Submitted: 2026-11-22 14:12 EST
# Intuition: Before the single value, pairs start at even indices and end at odd indices.
# Approach: Binary search for a value different from both neighbors. Otherwise
# use the midpoint's parity and matching neighbor to choose which half to search.
# Complexity: O(log n) time and O(1) extra space.

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        left = 0
        right = n
        if n == 0:
            return nums[0]

        while left <= right:
            mid = left + (right - left) // 2
            ln = mid - 1 if 0 <= mid - 1 < n else None
            rn = mid + 1 if 0 < mid + 1 <= n else None

            if (ln is not None and rn is not None and
                    nums[ln] != nums[mid] and nums[rn] != nums[mid]):
                return nums[mid]
            if ((ln is None and rn is not None and nums[rn] != nums[mid]) or
                    (rn is None and ln is not None and nums[ln] != nums[mid])):
                return nums[mid]

            if ((mid % 2 == 1 and nums[mid] == nums[ln]) or
                    (mid % 2 == 0 and nums[mid] == nums[rn])):
                left = mid + 1
            else:
                right = mid - 1
