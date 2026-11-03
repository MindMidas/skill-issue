# 283. Move Zeroes
# Problem: https://leetcode.com/problems/move-zeroes/
# Submitted: 2026-11-03 16:42 EST
# Intuition: Fill each zero with the next nonzero value to keep nonzero elements in their original order.
# Approach: Use write to find a zero and read to find the next nonzero, swap them, and keep both pointers moving forward.
# Complexity: O(n) time, O(1) extra space; neither pointer moves backward.

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        write = 0
        read = 0

        while True:

            # find first 0 we can write to
            while write < len(nums) and nums[write] != 0:
                write += 1
            
            # no zeros left, break
            if write == len(nums):
                break

            # find next nonzero after write
            read = max(read, write + 1)
            while read < len(nums) and nums[read] == 0:
                read += 1
            
            # only zeros remain after write
            if read == len(nums):
                break

            # fill the earliest zero with the next nonzero, preserving nonzero order
            nums[write], nums[read] = nums[read], nums[write]

            write += 1

        return
