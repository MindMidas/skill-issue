# 1004. Max Consecutive Ones III
# Problem: https://leetcode.com/problems/max-consecutive-ones-iii/
# Submitted: 2026-10-29 16:19 EDT
# Intuition: A window with at most k zeros can become all ones by flipping those zeros.
# Approach: Expand right, shrink left when there are too many zeros, and track the longest valid window.
# Complexity: O(n) time, O(1) extra space; each pointer moves through the array once.

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        # goal: find the longest run of ones after at most k flips
        # each zero in the window uses one flip
        # intuition: use a sliding window and keep track of zeros in the window

        zeros = 0
        left = 0
        max_len = 0

        # expand the window to the right
        for right in range(len(nums)):
            
            # if we see a zero, increment the count
            if nums[right] == 0:
                zeros += 1

            # shrink from the left until we have at most k zeros
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            # update max if larger
            max_len = max(max_len, right-left+1)
        
        return max_len
