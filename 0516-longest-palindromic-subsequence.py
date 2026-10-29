# 516. Longest Palindromic Subsequence
# Problem: https://leetcode.com/problems/longest-palindromic-subsequence/
# Submitted: 2026-10-29 11:25 EDT
# Intuition: Matching ends can both stay; otherwise, try skipping either end and keep the longer subsequence.
# Approach: DFS over left/right indices and memoize each interval's longest palindromic subsequence length.
# Complexity: O(n^2) time, O(n^2) space for memoization plus an O(n) recursion stack.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        # small input size: 1k chars max
        # goal: return the len of longest palindrome
        # rules: allowed to delete chars

        # intuition: we use two ptrs to process from left and right and explore valid choices

        memo = {}

        def dfs(left, right):
            
            if (left, right) in memo:
                return memo[(left, right)]

            # last valid char
            if left == right:
                return 1
            
            # no chars remaining
            if left > right:
                return 0

            # if the two chars are equal, include both and move inward
            if s[left] == s[right]:
                result = 2 + dfs(left+1, right-1)
            
            # chars don't match so return the greater option by moving left or right inward
            else:
                result = max(dfs(left+1, right), dfs(left, right-1))

            # memorize this result
            memo[(left, right)] = result

            return result
    
        return dfs(0, len(s) - 1)