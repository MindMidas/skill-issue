# 2357. Make Array Zero by Subtracting Equal Amounts
# Problem: https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
# Submitted: 2026-08-23 14:23 EDT
# Intuition: Each distinct positive value requires one subtraction level.
# Approach: Collect nonzero values in a set and return its size.
# Complexity: O(n) average time, O(n) space.

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        vals = set()

        for num in nums:
            if num != 0:
                vals.add(num)
        

        return len(vals)