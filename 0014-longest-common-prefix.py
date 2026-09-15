# 14. Longest Common Prefix
# Problem: https://leetcode.com/problems/longest-common-prefix/
# Submitted: 2026-09-15 15:29 EDT
# Intuition: A common prefix cannot extend past the shortest word.
# Approach: Choose the shortest word and compare its characters across every word.
# Complexity: O(n*m + m^2) worst-case time including prefix concatenation, O(m) space; m is shortest length.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        output = ""

        if not strs:
            return ""
       
        shortest = [0, len(strs[0])]
        
        for i, word in enumerate(strs):
            if len(word) < shortest[1]:
                shortest[1] = len(word)
                shortest[0] = i
            
        for i in range(shortest[1]):
            curr = strs[shortest[0]][i]

            for word in strs:
                if word[i] != curr:
                    return output
            
            output += curr
        
        return output


