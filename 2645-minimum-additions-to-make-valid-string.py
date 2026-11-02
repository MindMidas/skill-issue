# 2645. Minimum Additions to Make Valid String
# Problem: https://leetcode.com/problems/minimum-additions-to-make-valid-string/
# Submitted: 2026-11-02 14:21 EST
# Intuition: Follow the repeating abc pattern and insert any missing letters before consuming each character.
# Approach: Cycle through the expected letters, count mismatches as additions, and finish the last abc group.
# Complexity: O(n) time, O(1) extra space; each character needs at most two insertions before it.

class Solution:
    def addMinimum(self, word: str) -> int:
        
        # track the next expected character in abc
        pattern = ['a','b','c']
        expected = 0
        req_adds = 0
        
        # traverse word from left to right
        for char in word:

            # count missing letters until the current character fits
            while char != pattern[expected]:
                req_adds += 1
                expected = (expected + 1) % 3

            # consume this character and expect the next letter
            expected = (expected + 1) % 3

        # complete last abc group if we're still expecting b or c
        if expected != 0:
            req_adds += 3 - expected

        return req_adds
