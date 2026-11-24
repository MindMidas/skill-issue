# 983. Minimum Cost For Tickets
# Problem: https://leetcode.com/problems/minimum-cost-for-tickets/
# Submitted: 2026-11-24 12:00 EST
# Intuition: At each uncovered travel day, choose a one-, seven-, or thirty-day pass.
# Approach: Memoize the minimum cost from each travel-day index, advancing to
# the first day not covered by each candidate pass.
# Complexity: O(n) time and space. With unique integer travel days and fixed
# pass lengths, each search advances at most 30 travel days.


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        n = len(days)

        def nextValid(i, jump):
            start = days[i]
            while i < n and days[i] < start + jump:
                i += 1
            return i

        memo = {}

        def dfs(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            daily = costs[0] + dfs(nextValid(i, 1))
            weekly = costs[1] + dfs(nextValid(i, 7))
            monthly = costs[2] + dfs(nextValid(i, 30))
            result = min(daily, weekly, monthly)
            memo[i] = result
            return result

        return dfs(0)
