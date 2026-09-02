# 55. Jump Game
# Problem: https://leetcode.com/problems/jump-game/
# Submitted: 2026-09-02 13:17 EDT
# Intuition: A position is usable only while it lies within the farthest reachable index.
# Approach: Scan forward, reject gaps, and extend the farthest reach from each position.
# Complexity: O(n) time, O(n) space because nums[1:] creates a slice.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        furthest = nums[0]
        
        for i, num in enumerate(nums[1:], start=1):
            
            curr = i + num

            if i > furthest:
                return False 
            
            if curr > furthest:
                furthest = curr
                
        return True
