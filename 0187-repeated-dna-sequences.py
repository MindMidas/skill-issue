# 187. Repeated DNA Sequences
# Problem: https://leetcode.com/problems/repeated-dna-sequences/
# Submitted: 2026-11-25 11:44 EST
# Intuition: Track which ten-character windows have already appeared.
# Approach: Add each window to a seen set and repeated windows to a result set.
# Complexity: O(n) expected time and O(n) space for fixed-length windows.


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen = set()
        result = set()
        if len(s) <= 10:
            return []

        for i in range(len(s) - 9):
            ss = s[i:i + 10]
            if ss in seen:
                result.add(ss)
            seen.add(ss)

        return list(result)
