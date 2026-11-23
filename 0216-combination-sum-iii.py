# 216. Combination Sum III
# Problem: https://leetcode.com/problems/combination-sum-iii/
# Submitted: 2026-11-23 11:53 EST
# Intuition: Explore whether to include or skip each number from one through nine.
# Approach: Backtrack with a running sum and path, accepting exactly k numbers
# that sum to n. Stop when the sum is too large or no candidates remain.
# Complexity: O(2^9 + k * C(9, k)) time and O(k) auxiliary space, excluding output.


class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        if n > 45:
            return []
        result = []

        def dfs(i, total, path):
            if len(path) == k:
                if total == n:
                    result.append(path.copy())
                return
            if total >= n or i > 9:
                return

            path.append(i)
            dfs(i + 1, total + i, path)
            path.pop()
            dfs(i + 1, total, path)
            return

        dfs(1, 0, [])
        return result
