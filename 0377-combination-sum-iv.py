# 377. Combination Sum IV
# Problem: https://leetcode.com/problems/combination-sum-iv/
# Submitted: 2026-11-25 10:03 EST
# Intuition: Each next number creates another ordered way to reach the target.
# Approach: Memoize DFS by the running total, counting one way at the target
# and zero ways when the total exceeds it.
# Complexity: O(target * len(nums)) time and O(target) space.


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        memo = {}

        def dfs(total):
            if total == target:
                return 1
            if total > target:
                return 0
            if total in memo:
                return memo[total]

            ways = 0
            for n in nums:
                ways += dfs(total + n)
            memo[total] = ways
            return ways

        return dfs(0)
