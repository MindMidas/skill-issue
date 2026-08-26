# 704. Binary Search
# Problem: https://leetcode.com/problems/binary-search/
# Submitted: 2026-08-26 14:09 EDT
# Intuition: A sorted array lets each midpoint comparison discard half the search range.
# Approach: Move the low or high boundary until the target is found or the range is empty.
# Complexity: O(log n) time, O(1) space.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = low + (high - low) // 2

            if target == nums[mid]:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1