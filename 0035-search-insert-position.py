# 35. Search Insert Position
# Problem: https://leetcode.com/problems/search-insert-position/
# Submitted: 2026-11-07 13:16 EST
# Intuition: A normal binary search already narrows the answer down to the first valid insertion index.
# Approach: Search for the target and return left after the search if it is not found.
# Complexity: O(log n) time and O(1) space.

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1


        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
