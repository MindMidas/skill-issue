# 324. Wiggle Sort II
# Problem: https://leetcode.com/problems/wiggle-sort-ii/
# Submitted: 2026-11-02 10:52 EST
# Intuition: Alternate the smaller and larger halves; taking both backward keeps equal values apart.
# Approach: Sort, split at (n + 1) // 2, then fill even and odd positions with the reversed halves.
# Complexity: O(n log n) time, O(n) extra space for the slices.

class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # sort nums
        nums.sort()

        # get length to find midpoint
        n = len(nums)

        # the smaller half gets the extra element when n is odd
        mid = (n+1) // 2

        # reverse both halves when interleaving to keep equal values apart
        smaller = nums[:mid]
        larger = nums[mid:]

        # fill even indices with smaller values in reverse order
        nums[::2] = smaller[::-1]

        # fill odd indices with larger values in reverse order
        nums[1::2] = larger[::-1]

        return nums
