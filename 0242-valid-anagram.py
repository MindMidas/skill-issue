# 242. Valid Anagram
# Problem: https://leetcode.com/problems/valid-anagram/
# Submitted: 2026-08-11 15:36 EDT
# Intuition: Anagrams contain exactly the same number of every letter.
# Approach: Increment counts for one string and decrement for the other, then check all zeroes.
# Complexity: O(n) time, O(1) space for the fixed lowercase alphabet.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for a, b in zip(s, t):
            counts[ord(a) - 97] += 1
            counts[ord(b) - 97] -= 1

        return all(x == 0 for x in counts)