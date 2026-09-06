# 5. Longest Palindromic Substring
# Problem: https://leetcode.com/problems/longest-palindromic-substring/
# Submitted: 2026-09-06 16:47 EDT
# Intuition: A substring is palindromic when its endpoints match and its interior is too.
# Approach: Memoize palindrome checks for every interval and retain the longest sliced match.
# Complexity: O(n^3) worst-case time from substring slicing, O(n^2) space.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        known = {}

        def isPalindrome(i, j) -> bool:
            
            if (i,j) in known:
                return known[(i,j)]
            
            if i >= j:
                return True
            
            if s[i] != s[j]:
                return False
            
            known[(i,j)] = isPalindrome(i+1, j-1)
            
            return known[(i,j)]

        longest_pal = ""

        for i in range(len(s)):
            for j in range(i,len(s)):

                if isPalindrome(i,j):
                    curr_pal = s[i:j+1]

                    if len(curr_pal) > len(longest_pal):
                        longest_pal = curr_pal

        return longest_pal