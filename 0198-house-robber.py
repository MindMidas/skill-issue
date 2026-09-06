# 198. House Robber
# Problem: https://leetcode.com/problems/house-robber/
# Submitted: 2026-09-06 16:07 EDT
# Intuition: At each house, choose between robbing it and skipping to the next.
# Approach: Memoize the best total from each house using take-or-skip recursion.
# Complexity: O(n) time, O(n) space.

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        sub_solutions = {}
        def dfs(house: int) -> int:

            if house >= len(nums):
                return 0
            
            if house in sub_solutions:
                return sub_solutions[house]
            
            sub_solutions[house] = max(nums[house] + dfs(house+2), dfs(house+1))

            return sub_solutions[house]

        return dfs(0)