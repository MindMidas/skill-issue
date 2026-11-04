# 136. Single Number
# Problem: https://leetcode.com/problems/single-number/
# Submitted: 2026-11-04 16:07 EST
# Intuition: XOR cancels each pair of equal numbers, leaving the unique value.
# Approach: XOR every number into a running result.
# Complexity: O(n) time and O(1) space.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0

        for n in nums:
            result ^= n

        return result
