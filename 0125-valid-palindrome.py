# 125. Valid Palindrome
# Problem: https://leetcode.com/problems/valid-palindrome/
# Submitted: 2026-08-23 16:30 EDT
# Intuition: A palindrome reads the same after removing punctuation and ignoring case.
# Approach: Build a lowercase alphanumeric string and compare it with its reverse.
# Complexity: O(n^2) worst-case time from string concatenation, O(n) space.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ispalindrome = False

        clean = "" 

        for c in s:
            if c.isalnum():
                clean+=c.lower()

        return clean == clean[::-1]

