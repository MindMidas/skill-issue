# 213. House Robber II
# Problem: https://leetcode.com/problems/house-robber-ii/
# Submitted: 2026-09-06 16:16 EDT
# Intuition: The circular street prevents robbing both the first and last houses.
# Approach: Memoize take-or-skip decisions twice, excluding one endpoint each time.
# Complexity: O(n) time, O(n) space.

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        best = {}

        def dfs(house: int, exclude: int) -> int:

            if house >= len(nums):
                return 0
            if house == exclude:
                return 0
            
            if (house, exclude) not in best:
                best[(house, exclude)] = max(nums[house] + dfs(house+2, exclude), dfs(house+1, exclude))
            
            return best[(house, exclude)]
        
        return max(dfs(0, len(nums) - 1), dfs(1, 0))