# 2483. Minimum Penalty for a Shop
# Problem: https://leetcode.com/problems/minimum-penalty-for-a-shop/
# Submitted: 2026-11-09 14:41 EST
# Intuition: A closing hour's penalty combines empty open hours before it and customer visits after it.
# Approach: Build prefix penalties for staying open and suffix penalties for staying closed, then choose the earliest hour with the smallest combined penalty.
# Complexity: O(n) time and O(n) space.

class Solution:
    def bestClosingTime(self, customers: str) -> int:

        # intuition: we create open and closed arrays where:
        # open tracks the penalty based on items to the left and
        # closed tracks penalties based on everything to the right

        n = len(customers)
        closed_pen = [1 if customers[n-1] == 'Y' else 0]
        open_pen = [1 if customers[0] == 'N' else 0]

        # closed penalties
        for i in range(n-2, -1, -1):
            closed_pen.append(closed_pen[-1] + (1 if customers[i] == 'Y' else 0))
        closed_pen.reverse()

        # open penalties
        for i in range(1, n):
            open_pen.append(open_pen[-1] + (1 if customers[i] == 'N' else 0))

        # account for closing at hour n or 0
        closed_pen.append(0)
        open_pen.insert(0, 0)

        # find cheapest closing hour
        min_cost = float("inf")
        min_index = -1

        for i in range(n+1):
            if closed_pen[i] + open_pen[i] < min_cost:
                min_cost = closed_pen[i] + open_pen[i]
                min_index = i

        return min_index
