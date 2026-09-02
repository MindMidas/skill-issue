# 53. Maximum Subarray
# Problem: https://leetcode.com/problems/maximum-subarray/
# Submitted: 2026-09-02 12:23 EDT
# Intuition: The best subarray ending here either extends the previous one or starts here.
# Approach: Run Kadane's recurrence, tracking the best current sum and overall sum.
# Complexity: O(n) time, O(n) space because nums[1:] creates a slice.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current = nums[0]
        best = nums[0]

        for num in nums[1:]:

            current = max(num, current + num)
            best = max(current, best)
        
        return best
