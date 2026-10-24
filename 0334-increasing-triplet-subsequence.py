# 334. Increasing Triplet Subsequence
# Problem: https://leetcode.com/problems/increasing-triplet-subsequence/
# Submitted: 2026-10-24 14:50 EDT
# Intuition: second already has an earlier smaller value; lowering first later doesn't invalidate that pair.
# Approach: Keep the smallest first and second candidates; a later number greater than second completes the triplet.
# Complexity: O(n) time, O(1) extra space.

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
    
        first = None
        second = None

        for n in nums:
            if first is None or n <= first:
                first = n
            elif second is None or n <= second:
                second = n
            else:
                return True

        return False

            

