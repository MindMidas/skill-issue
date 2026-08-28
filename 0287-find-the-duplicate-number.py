# 287. Find the Duplicate Number
# Problem: https://leetcode.com/problems/find-the-duplicate-number/
# Submitted: 2026-08-28 17:19 EDT
# Intuition: Treating values as next indices creates a cycle whose entry is the duplicate.
# Approach: Use Floyd's slow/fast pointers to meet, then walk together to the cycle entry.
# Complexity: O(n) time, O(1) space.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[0]
        fast = nums[0]

        while True:

            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if slow == fast:
                break
        
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
        
