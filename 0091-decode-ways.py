# 91. Decode Ways
# Problem: https://leetcode.com/problems/decode-ways/
# Submitted: 2026-11-21 14:55 EST
# Intuition: Try decoding one digit or two digits from each position.
# Approach: Memoize the number of valid decodings from each index. Reject
# leading zeros and only take two digits when their value is between 10 and 26.
# Complexity: O(n) time and O(n) space for memoization and recursion.


class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i == len(s):
                return 1
            if i in memo:
                return memo[i]

            ways = 0
            if s[i] == "0":
                return 0
            ways += dfs(i + 1)

            if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                ways += dfs(i + 2)

            memo[i] = ways
            return ways

        return dfs(0)
