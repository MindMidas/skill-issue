# 1648. Sell Diminishing-Valued Colored Balls
# Problem: https://leetcode.com/problems/sell-diminishing-valued-colored-balls/
# Submitted: 2026-11-02 12:27 EST
# Intuition: Always sell the highest-valued balls, grouping equal inventories to sell whole price levels at once.
# Approach: Use a max heap of inventory groups, sum batches with arithmetic series, and merge groups at equal levels.
# Complexity: O(n + u log u) time, O(u) extra space, where u is the number of distinct starting inventories.

import heapq
from collections import Counter

class Solution:
    def maxProfit(self, inventory: list[int], orders: int) -> int:

        # goal: maximize the value of the balls sold
        # each ball sells for the current number of balls of its color
        # sell the highest group down to the next level in one batch

        # count how many colors have the same number of balls
        freq = Counter(inventory)

        # create heap, we don't really care about colors for the solution
        # store (-balls, number of colors) to process tied colors together
        max_heap = [(-x, count) for x, count in freq.items()]
        heapq.heapify(max_heap)

        max_val= 0

        while orders != 0:

            # pop largest, peek next largest, and get diff
            neg_largest, colors = heapq.heappop(max_heap)
            largest = -neg_largest

            if max_heap:
                next_largest = -max_heap[0][0]
            else:
                next_largest = 0

            difference = largest - next_largest

            # total orders needed to sell all colors down to next largest
            batch_size = difference * colors

            if orders >= batch_size:

                # total orders for this batch
                curr_orders = batch_size

                # lowest price in this batch; from 6 down to 3, sell at 6, 5, and 4
                last = next_largest + 1

                # add average price * curr_orders to max_val (since numbers decrease evenly)
                max_val += (largest + last) * difference // 2 * colors

                # subtract the sold batch and lower this group to the next level
                orders -= curr_orders
                remaining = next_largest

                # merge these colors with the next largest group
                if max_heap:
                    _, next_colors = heapq.heappop(max_heap)
                    if remaining > 0:
                        heapq.heappush(max_heap, (-remaining, colors + next_colors))

            else:

                # sell as many complete levels as possible across all colors
                full_levels = orders // colors

                # remaining orders after selling complete levels
                remainder = orders % colors

                # lowest price sold per color across the complete levels
                last = largest - full_levels + 1

                # add average price * full_levels for all colors
                max_val += (largest + last) * full_levels // 2 * colors

                # sell remaining balls at the next available price
                max_val += remainder * (largest - full_levels)

                orders = 0

        return max_val % (10**9 + 7)
