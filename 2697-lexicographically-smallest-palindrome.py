# 2697. Lexicographically Smallest Palindrome
# Problem: https://leetcode.com/problems/lexicographically-smallest-palindrome/
# Submitted: 2026-09-21 19:30 EDT
# Intuition: Each mismatched mirrored pair needs one change; choose its smaller letter.
# Approach: Use two pointers on a character list, replace the larger letter, then join.
# Complexity: O(n) time, O(n) space.

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
        s = list(s)
        left = 0
        right = len(s) - 1

        while left <= right:

            if s[left] > s[right]:
                s[left] = s[right]
            elif s[left] < s[right]:
                s[right] = s[left]
    
            left += 1
            right -= 1

        return "".join(s)