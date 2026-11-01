# 2414. Length of the Longest Alphabetical Continuous Substring
# Problem: https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/
# Submitted: 2026-11-01 12:29 EST
# Intuition: An alphabetical run continues only when each letter is exactly one after the previous letter.
# Approach: Track the run's start, record its length when it breaks, and check the final run after the loop.
# Complexity: O(n) time, O(1) extra space.

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
        # use sliding window
        # adjacent letters must differ by exactly 1
        # maintain longest window size

        left = 0
        longest = 0

        for i in range(1, len(s)):

            # the alphabetical run breaks here
            if ord(s[i]) - ord(s[i-1]) != 1:
                longest = max(longest, i - left)
                left = i # start new window
            
        # check last window
        longest = max(longest, len(s) - left)

        return longest
