# 45. Jump Game II
# Problem: https://leetcode.com/problems/jump-game-ii/
# Submitted: 2026-09-02 14:00 EDT
# Intuition: All positions reachable with the current jump form one greedy frontier.
# Approach: Track the farthest next reach and count a jump whenever the current frontier ends.
# Complexity: O(n) time, O(1) space.

class Solution:
    def jump(self, nums: List[int]) -> int:
    
        jumps = 0
        curr_end = 0
        farthest = 0

        for i in range(len(nums) - 1):

            farthest = max(farthest, i + nums[i])

            if i == curr_end:
                curr_end = farthest
                jumps += 1
                

        return jumps

