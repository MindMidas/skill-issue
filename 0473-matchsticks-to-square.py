# 473. Matchsticks to Square
# Problem: https://leetcode.com/problems/matchsticks-to-square/
# Submitted: 2026-11-25 12:57 EST
# Intuition: Assign each matchstick to one of four equal-length sides.
# Approach: Sort descending, backtrack over sides without exceeding the target,
# and memoize failed states using sorted side lengths to merge symmetric cases.
# Complexity: O(4^n + n log n) worst-case time and O(4^n) memoization space.


class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        memo = {}
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        target = total // 4
        sides = [0, 0, 0, 0]
        matchsticks.sort(key=lambda x: -x)

        def dfs(i):
            if i == len(matchsticks):
                return True

            state = (i, tuple(sorted(sides)))
            if state in memo:
                return False

            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[j] -= matchsticks[i]

            memo[state] = False
            return False

        return dfs(0)
