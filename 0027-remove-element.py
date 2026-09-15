# 27. Remove Element
# Problem: https://leetcode.com/problems/remove-element/
# Submitted: 2026-09-15 16:18 EDT
# Intuition: Valid elements can overwrite the array's prefix as they are encountered.
# Approach: Use a write count to compact all elements unequal to val in place.
# Complexity: O(n) time, O(1) space.

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        total_valid = 0

        for num in nums:

            if num != val:
                nums[total_valid] = num
                total_valid += 1
        
        return total_valid