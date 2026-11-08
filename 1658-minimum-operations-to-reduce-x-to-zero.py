# 1658. Minimum Operations to Reduce X to Zero
# Problem: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# Submitted: 2026-11-08 17:11 EST
# Intuition: Removing the fewest elements from the ends means keeping the longest middle subarray with sum total - x.
# Approach: Use a sliding window over the positive values to find the longest subarray with the required sum, then subtract its length from the array length.
# Complexity: O(n) time and O(1) extra space.

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:

        total = sum(nums)
        keep = total - x

        left = 0
        right = 0

        window_sum = 0
        max_len = -1

        if keep < 0:
            return -1
        if keep == 0:
            return len(nums)

        while right < len(nums):

            # grow window right
            window_sum += nums[right]

            # shrink window by moving left ptr
            while left <= right and window_sum > keep:
                window_sum -= nums[left]
                left += 1

            if window_sum == keep:
                max_len = max(max_len, right - left + 1)

            right += 1

        # no valid window found
        if max_len == -1:
            return -1

        return len(nums) - max_len
