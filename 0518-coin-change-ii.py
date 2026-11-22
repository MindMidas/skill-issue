# 518. Coin Change II
# Problem: https://leetcode.com/problems/coin-change-ii/
# Submitted: 2026-11-22 15:50 EST
# Intuition: Build combinations by adding one denomination at a time.
# Approach: Set dp[0] to one and process coins in the outer loop. For each
# reachable amount, add the combinations formed by including the current coin.
# Complexity: O(amount * len(coins)) time and O(amount) space.


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[amount]
