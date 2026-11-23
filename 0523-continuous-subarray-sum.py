# 523. Continuous Subarray Sum
# Problem: https://leetcode.com/problems/continuous-subarray-sum/
# Submitted: 2026-11-23 16:05 EST
# Intuition: Equal prefix-sum remainders identify a subarray divisible by k.
# Approach: Store the earliest index for each remainder and check that repeated
# remainders are at least two indices apart.
# Complexity: O(n) expected time and O(min(n, k)) space.


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix = 0
        seen = {0: -1}
        for i, num in enumerate(nums):
            prefix += num
            remainder = prefix % k
            if remainder in seen:
                if i - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = i

        return False
