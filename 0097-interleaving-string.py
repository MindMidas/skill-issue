# 97. Interleaving String
# Problem: https://leetcode.com/problems/interleaving-string/
# Submitted: 2026-11-20 12:01 EST
# Intuition: Track positions in both strings and try both choices when their
# next characters match the next character in the target.
# Approach: Reject unequal total lengths, then memoize DFS results for each
# pair of consumed prefix lengths.
# Complexity: O((m + 1) * (n + 1)) time and space for source lengths m and n.


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        i = 0
        j = 0
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(s1) and j == len(s2):
                return True

            if i < len(s1) and s1[i] == s3[i + j]:
                if dfs(i + 1, j):
                    memo[(i, j)] = True
                    return True

            if j < len(s2) and s2[j] == s3[i + j]:
                if dfs(i, j + 1):
                    memo[(i, j)] = True
                    return True

            memo[(i, j)] = False
            return False

        return dfs(0, 0)
