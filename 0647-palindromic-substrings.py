# 647. Palindromic Substrings
# Problem: https://leetcode.com/problems/palindromic-substrings/
# Submitted: 2026-09-06 17:04 EDT
# Intuition: Every palindrome expands around either one character or a gap.
# Approach: Expand around each odd and even center and count every matching span.
# Complexity: O(n^2) time, O(1) space.

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        total = 0

        for center in range(len(s)):
            # odd
            l = r = center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1

            # even
            l, r = center, center + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1
        
        return total