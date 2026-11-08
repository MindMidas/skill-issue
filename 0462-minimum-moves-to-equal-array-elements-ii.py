# 462. Minimum Moves to Equal Array Elements II
# Problem: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# Submitted: 2026-11-08 16:39 EST
# Intuition: A median minimizes the sum of absolute distances to all array elements.
# Approach: Sort the array, choose its middle element, and sum each element's distance to that median.
# Complexity: O(n log n) time and O(n) auxiliary space for Python's sort.

class Solution:
    def minMoves2(self, nums: list[int]) -> int:

        # sort nums
        nums.sort()
        n = len(nums)

        # get median
        median = nums[n//2]
        total_moves = 0

        # calc moves
        for n in nums:
            total_moves += abs(n-median)

        return total_moves
