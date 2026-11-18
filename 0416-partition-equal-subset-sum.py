# 416. Partition Equal Subset Sum
# Problem: https://leetcode.com/problems/partition-equal-subset-sum/
# Submitted: 2026-11-18 13:22 EST
# Intuition: An equal partition exists when a subset sums to half the total.
# Approach: Reject odd totals, then maintain the achievable sums up to the
# target, using each number once by reading from the previous set.
# Complexity: O(n * target) expected time and O(target) space.


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        possible = {0}
        for n in nums:
            new_possible = set(possible)
            for size in possible:
                if size + n <= target:
                    new_possible.add(size + n)
            possible = new_possible
            if target in possible:
                return True

        return False
