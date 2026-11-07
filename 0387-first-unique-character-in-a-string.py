# 387. First Unique Character in a String
# Problem: https://leetcode.com/problems/first-unique-character-in-a-string/
# Submitted: 2026-11-07 18:51 EST
# Intuition: The first unique character is the earliest character whose total frequency is one.
# Approach: Count each character, then scan the string in order and return the first index with frequency one, or -1 if none exists.
# Complexity: O(n) time and O(1) space for the fixed lowercase English alphabet.

class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq = {}

        # log freq per char
        for c in s:
            freq[c] = freq.get(c,0) + 1

        # return first char with freq == 1
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i

        # no freq == 1
        return -1
