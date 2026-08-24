# 3. Longest Substring Without Repeating Characters
# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Submitted: 2026-08-24 13:51 EDT
# Intuition: A duplicate inside the window forces its left boundary past the previous copy.
# Approach: Store last-seen indices and jump the window's left boundary forward as needed.
# Complexity: O(n) time, O(min(n, a)) space; a is the alphabet size.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        best = 0
        seen = {}
        left = 0

        for right, char in enumerate(s):
            
            # if we've seen this char before move left to start of new substring
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            
            # update char in seen to new index
            seen[char] = right

            # get best
            best = max(best, right-left+1)

        return best