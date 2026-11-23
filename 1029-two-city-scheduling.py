# 1029. Two City Scheduling
# Problem: https://leetcode.com/problems/two-city-scheduling/
# Submitted: 2026-11-23 13:12 EST
# Intuition: Favor city A for the people whose A cost is cheapest relative to B.
# Approach: Sort by A minus B cost, send the first half to A and the rest to B,
# and sum the chosen costs.
# Complexity: O(n log n) time and O(n) space.


class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        diff = sorted(costs, key=lambda cost: cost[0] - cost[1])
        n = len(diff) // 2
        total = 0
        for i in range(len(diff)):
            if i < n:
                total += diff[i][0]
            else:
                total += diff[i][1]

        return total
