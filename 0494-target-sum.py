# 494. Target Sum
# Problem: https://leetcode.com/problems/target-sum/
# Submitted: 2026-09-07 13:05 EDT
# Intuition: The remaining choices depend only on the index and current sum.
# Approach: Memoize the number of ways after choosing plus or minus for each value.
# Complexity: O(n*(S + 1)) time and space; S = sum(abs(x) for x in nums).

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dfs(i, curr_sum) -> int:

            if i == len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0

            if (i,curr_sum) in memo:
                return memo[(i,curr_sum)]
            
            memo[(i, curr_sum)] = dfs(i+1, curr_sum + nums[i]) + dfs(i+1, curr_sum - nums[i])
            return memo[(i,curr_sum)]
        
        return dfs(0, 0)