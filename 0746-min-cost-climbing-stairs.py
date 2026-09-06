# 746. Min Cost Climbing Stairs
# Problem: https://leetcode.com/problems/min-cost-climbing-stairs/
# Submitted: 2026-09-06 15:01 EDT
# Intuition: The cheapest route from a step uses the cheaper of the next two routes.
# Approach: Memoize each step's cost and take the cheaper start at step 0 or 1.
# Complexity: O(n) time, O(n) space.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        sub_solutions = {}

        def dfs(step: int) -> int:

            if step >= len(cost):
                return 0

            if step in sub_solutions:
                return sub_solutions[step]
            
            sub_solutions[step] = min(dfs(step+1),dfs(step+2)) + cost[step]

            return sub_solutions[step]
        
        return min(dfs(0), dfs(1))