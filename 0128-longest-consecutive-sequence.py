# 128. Longest Consecutive Sequence
# Problem: https://leetcode.com/problems/longest-consecutive-sequence/
# Submitted: 2026-08-12 12:56 EDT
# Intuition: A consecutive run only needs counting from a value with no predecessor.
# Approach: Put values in a set and extend runs only from their smallest element.
# Complexity: O(n) average time, O(n) space.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums);
        longest = 0;

        for num in nums_set:

            if (num - 1) in nums_set:
                continue;
            
            curr = num;
            length = 0;

            while curr in nums_set:
                length += 1;
                curr += 1;

            longest = max(longest, length);
        
        return longest;