# 70. Climbing Stairs
# Problem: https://leetcode.com/problems/climbing-stairs/
# Submitted: 2026-09-06 14:47 EDT
# Intuition: Each step can be reached by taking one or two steps from the current position.
# Approach: Memoize the number of ways to reach the top from each step.
# Complexity: O(n) time, O(n) space.

class Solution:
    def climbStairs(self, n: int) -> int:
        
        solutions = {}

        def dfs(step: int) -> int:
            
            if step == n:
                return 1
            if step > n:
                return 0
            
            if step in solutions:
                return solutions[step]
            else:
                solutions[step] = dfs(step+1) + dfs(step+2)

            return solutions[step]
        
        return dfs(0)