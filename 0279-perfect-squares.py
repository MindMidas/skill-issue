# 279. Perfect Squares
# Problem: https://leetcode.com/problems/perfect-squares/
# Submitted: 2026-11-26 11:26 EST
# Intuition: An optimal sum uses one square plus an optimal solution for the remainder.
# Approach: Precompute squares and fill a bottom-up table of minimum square
# counts for every sum from zero through n.
# Complexity: O(n * sqrt(n)) time and O(n) space.

import math


class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = []
        for i in range(1, math.isqrt(n) + 1):
            perfect_squares.append(i * i)

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for remaining in range(1, n + 1):
            for ps in perfect_squares:
                if ps > remaining:
                    break
                dp[remaining] = min(dp[remaining], 1 + dp[remaining - ps])

        return dp[n]
