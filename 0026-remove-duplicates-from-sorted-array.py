# 26. Remove Duplicates from Sorted Array
# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Submitted: 2026-09-15 16:12 EDT
# Intuition: Equal values are adjacent in a sorted array, so only changes need keeping.
# Approach: Track the previous value and write each new value into the next free position.
# Complexity: O(n) time, O(1) space.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        valid_hits = 0
        prev_value = None

        for num in nums:
            
            if prev_value is None or prev_value != num:
                nums[valid_hits] = num
                valid_hits += 1
                prev_value = num

        return valid_hits
