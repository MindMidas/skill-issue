# 740. Delete and Earn
# Problem: https://leetcode.com/problems/delete-and-earn/
# Submitted: 2026-11-01 16:40 EST
# Intuition: Combine points for each value; choosing a value blocks its neighbors, like House Robber.
# Approach: Memoize the best score from x onward, choosing between taking x and jumping to x + 2 or skipping to x + 1.
# Complexity: O(n + M) time, O(M) extra space including recursion, where M = max(nums).

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        
        # goal: return the maximum points earned
        # taking a value removes its neighbors, so combine all copies into one score

        # store points per number
        points = {}
        for num in nums:
            points[num] = points.get(num,0) + num  

        # consider values up to the largest number
        max_num = max(nums)
        memo = {}

        def dfs(x):

            # no more nums to consider
            if x > max_num:
                return 0
            
            # reuse the best score from this value onward
            if x in memo:
                return memo[x]
            
            # taking x skips x + 1; otherwise move to the next value
            take = points.get(x,0) + dfs(x+2)
            skip = dfs(x+1)

            # save and return the best result
            memo[x] = max(take,skip)

            return memo[x]

        
        return dfs(1)
