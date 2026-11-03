# 219. Contains Duplicate II
# Problem: https://leetcode.com/problems/contains-duplicate-ii/
# Submitted: 2026-11-03 18:01 EST
# Intuition: Only the previous k elements can form a valid duplicate pair with the current value.
# Approach: Keep those values in a sliding-window set, check for a match, and remove the oldest value as the window moves.
# Complexity: O(n) expected time, O(min(n, k + 1)) extra space, including the newly added value.

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        window = set()
        left = 0

        for right in range(len(nums)):
            
            # a match among the previous k elements gives a valid pair
            if nums[right] in window:
                return True

            # include this value for upcoming checks
            window.add(nums[right])     

            # remove the oldest value to keep at most k for the next check
            if right - left >= k:
                window.remove(nums[left])
                left += 1
        
        # no equal values were close enough
        return False
