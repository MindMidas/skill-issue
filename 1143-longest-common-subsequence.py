# 1143. Longest Common Subsequence
# Problem: https://leetcode.com/problems/longest-common-subsequence/
# Submitted: 2026-11-23 16:24 EST
# Intuition: Matching characters extend a common subsequence. A mismatch requires
# trying a skipped character from either string.
# Approach: Memoize the best subsequence length for each pair of string indices.
# Complexity: O(m * n) time and O(m * n + m + n) space for lengths m and n.


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                result = 1 + dfs(i + 1, j + 1)
            else:
                result = max(dfs(i + 1, j), dfs(i, j + 1))
            memo[(i, j)] = result
            return result

        return dfs(0, 0)
