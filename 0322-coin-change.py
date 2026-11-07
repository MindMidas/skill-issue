# 322. Coin Change
# Problem: https://leetcode.com/problems/coin-change/
# Submitted: 2026-11-07 18:44 EST
# Intuition: The best way to make an amount ends with one coin and an optimal solution for the remaining amount.
# Approach: Build a DP array of minimum coin counts from zero through amount, trying every coin for each subtotal. Return -1 if the target remains unreachable.
# Complexity: O(amount * len(coins)) time and O(amount) space.

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        # store min coins needed for each amount
        min_coins = [float("inf")] * (amount + 1)
        min_coins[0] = 0

        # calc min coins for each amount
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    min_coins[i] = min(min_coins[i], 1 + min_coins[i - c])

        # return -1 if amount cant be made
        if min_coins[amount] == float("inf"):
            return -1

        return min_coins[amount]
