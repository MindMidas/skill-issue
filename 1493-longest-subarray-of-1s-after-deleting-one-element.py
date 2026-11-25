# 1493. Longest Subarray of 1's After Deleting One Element
# Problem: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# Submitted: 2026-11-25 14:07 EST
# Intuition: A window with at most one zero becomes all ones after one deletion.
# Approach: Track the last zero and move the left boundary beyond it when
# another zero appears. Subtract one from each window length for the deletion.
# Complexity: O(n) time and O(1) extra space.


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        best = 0
        left = 0
        zero = -1
        for right in range(len(nums)):
            if nums[right] == 0:
                if zero != -1:
                    left = zero + 1
                zero = right
            best = max(best, right - left)

        return best
