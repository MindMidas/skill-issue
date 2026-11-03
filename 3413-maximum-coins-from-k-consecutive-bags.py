# 3413. Maximum Coins From K Consecutive Bags
# Problem: https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/
# Submitted: 2026-11-03 10:58 EST
# Intuition: An optimal window can align with an interval boundary, so check both starting and ending boundaries.
# Approach: Sort intervals and slide windows ending at each right boundary; mirror coordinates to cover starting boundaries too.
# Complexity: O(n log n) time, O(n) extra space; each sliding-window pass is O(n).

class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:

        # scan whole intervals instead of visiting every bag position

        # sort intervals by starting position
        coins.sort(key=lambda x: x[0])

        def sliding_window(coins):

            left = 0
            max_coins = 0
            total = 0

            for right in range(len(coins)):

                # unpack current interval
                l, r, count = coins[right]

                # add all coins from curr interval
                total += (r - l + 1) * count

                # window of k bags ending at r
                window_start = r - k + 1

                # remove intervals completely outside the window
                while left <= right and coins[left][1] < window_start:
                    a, b, c = coins[left]
                    total -= (b - a + 1) * c
                    left += 1

                # keep total intact; subtract the part before window_start for this candidate
                curr_total = total

                if left <= right:
                    a, b, c = coins[left]
                    excluded = max(0, window_start - a)
                    curr_total -= excluded * c

                # update max coins
                max_coins = max(max_coins, curr_total)

            return max_coins

        # check windows ending at interval ends
        max_coins = sliding_window(coins)

        # reverse coordinates to check windows starting at interval starts
        reversed_coins = [[-r, -l, count] for l, r, count in reversed(coins)]

        # return max coins across both directions
        return max(max_coins, sliding_window(reversed_coins))
