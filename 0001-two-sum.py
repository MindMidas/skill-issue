# 1. Two Sum
# Problem: https://leetcode.com/problems/two-sum/
# Submitted: 2026-08-11 15:58 EDT
# Intuition: For each value, its needed partner is target minus that value.
# Approach: Look up the complement in a map of previous values, then store the current index.
# Complexity: O(n) average time, O(n) space.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            
            need = target - num
            
            if need in seen:
                return [seen[need], i]
            
            seen[num] = i


        return None
