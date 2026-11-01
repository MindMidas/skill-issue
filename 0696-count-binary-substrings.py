# 696. Count Binary Substrings
# Problem: https://leetcode.com/problems/count-binary-substrings/
# Submitted: 2026-11-01 12:49 EST
# Intuition: Adjacent runs of zeros and ones form min(previous length, current length) valid substrings.
# Approach: Track two run lengths, count each pair when the next run starts, and add the final pair.
# Complexity: O(n) time, O(1) extra space.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        # valid substrings take equal counts from two adjacent groups
        # the smaller group size tells us how many valid substrings they form

        prev_count = 0
        curr_count = 1
        result = 0

        for i in range(1, len(s)):

            # finish counting the previous pair, then start the new group
            if s[i] != s[i-1]:
                result += min(prev_count, curr_count)
                prev_count = curr_count
                curr_count = 1
            else:
                curr_count += 1 # increase current group size
        
        # count the final pair of groups
        result += min(prev_count, curr_count)

        return result
