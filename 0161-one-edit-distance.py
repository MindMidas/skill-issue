# 161. One Edit Distance
# Problem: https://leetcode.com/problems/one-edit-distance/
# Submitted: 2026-11-09 17:57 EST
# Intuition: At the first mismatch, the string lengths determine whether to delete, replace, or insert one character.
# Approach: Reject identical strings and length gaps over one. Scan the common prefix, compare the suffixes after the required edit, and otherwise check for one leftover character.
# Complexity: O(n + m) time and O(n + m) space for string slices and concatenations.

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        # base case
        if s == t or abs(len(s) - len(t)) > 1:
            return False

        for i in range(min(len(s),len(t))):

            if s[i] == t[i]:
                continue

            # try deleting curr char
            if len(s) > len(t):
                return s[i+1:] == t[i:]

            # try replacing curr char
            elif len(t) == len(s):
                return t[i] + s[i+1:] == t[i:]

            # try inserting new char
            elif len(s) < len(t):
                return t[i] + s[i:] == t[i:]

            # None work so return False
            else:
                return False

        # handle any leftover char
        return abs(len(s) - len(t)) == 1
