# 209. Minimum Size Subarray Sum
# Problem: https://leetcode.com/problems/minimum-size-subarray-sum/
# Submitted: 2026-11-19 15:08 EST
# Intuition: Positive numbers let us shrink a valid window to find its shortest length.
# Approach: Extend the right boundary, then move the left boundary while the
# window sum meets the target. Return zero if no window qualifies.
# Complexity: O(n) time and O(1) extra space.


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        right = 0
        min_subarray = float("inf")
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target and left <= right:
                min_subarray = min(min_subarray, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if min_subarray == float("inf") else min_subarray
