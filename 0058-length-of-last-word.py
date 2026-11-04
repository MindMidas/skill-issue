# 58. Length of Last Word
# Problem: https://leetcode.com/problems/length-of-last-word/
# Submitted: 2026-11-04 11:53 EST
# Intuition: Keep the last word's length through any trailing spaces.
# Approach: Scan left to right and reset the count when a letter starts a new word.
# Complexity: O(n) time, O(1) extra space.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        possible_end = False
        last_len = 0

        for char in s:

            # keep the last length until another word begins
            if char == ' ':
                possible_end = True
                continue

            # reset when the next word starts
            if possible_end:
                last_len = 0
                possible_end = False

            # count this letter
            last_len += 1


        return last_len
