# 217. Contains Duplicate
# Problem: https://leetcode.com/problems/contains-duplicate/
# Submitted: 2026-08-11 15:13 EDT
# Intuition: A duplicate is any value already encountered earlier in the scan.
# Approach: Store values in a set and return as soon as a value repeats.
# Complexity: O(n) average time, O(n) space.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set();
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False;
