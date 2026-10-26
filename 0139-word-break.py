# 139. Word Break
# Problem: https://leetcode.com/problems/word-break/
# Submitted: 2026-10-26 13:44 EDT
# Intuition: Once a dictionary word matches, only the remaining suffix needs to be segmented.
# Approach: DFS from each starting index, try matching dictionary words, and memoize whether the suffix can be segmented.
# Complexity: O(n*k*L) time, O(n) extra space; n = string length, k = dictionary size, L = longest word length.

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        memo = {}

        def dfs(i):
            
            # entire string segmented 
            if i == len(s):
                return True
            
            # return prev calculated result
            if i in memo:
                return memo[i]
            
            # try every possible word at this index
            for word in wordDict:

                # check if word matches current substring
                if s[i:i+len(word)] == word:

                    # try segmenting the remaining string
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True
            
            # no valid segmentation found
            memo[i] = False
            return False
        
        return dfs(0)
