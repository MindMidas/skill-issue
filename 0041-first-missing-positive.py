# 41. First Missing Positive
# Problem: https://leetcode.com/problems/first-missing-positive/
# Submitted: 2026-10-25 16:13 EDT
# Intuition: With n elements, the answer is in 1..n+1; place each valid value x at index x-1.
# Approach: Swap values into their matching positions, skipping duplicates, then return the first mismatched index plus one.
# Complexity: O(n) time, O(1) extra space; each swap fixes a position and the final scan is linear.

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        
        n = len(nums)
        i = 0

        # place valid numbers at valid index
        while i < n:
            # swap 
            if 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                # increment 
                i += 1

        # return smallest positive int where val is not at right index
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1

        # else handle edge case where smallest is num after largest
        return n + 1
