# 930. Binary Subarrays With Sum
# Problem: https://leetcode.com/problems/binary-subarrays-with-sum/
# Submitted: 2026-11-24 17:26 EST
# Intuition: Leading zeros create additional valid starts for the same window sum.
# Approach: Shrink excess sum, count removable leading zeros when the goal is
# reached, and include those alternative starts in the count at each right edge.
# Complexity: O(n) time and O(1) extra space.


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        left = 0
        ways = 0
        total = 0
        leading_zeros = 0

        for right in range(len(nums)):
            total += nums[right]
            while total > goal:
                total -= nums[left]
                left += 1
                leading_zeros = 0

            while left < right and total == goal and nums[left] == 0:
                left += 1
                leading_zeros += 1

            if left <= right and total == goal:
                ways += 1 + leading_zeros
        return ways
