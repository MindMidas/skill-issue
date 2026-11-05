# 140. Word Break II
# Problem: https://leetcode.com/problems/word-break-ii/
# Submitted: 2026-11-05 14:47 EST
# Intuition: Different word choices can lead to the same suffix, so reuse its sentences.
# Approach: Try each dictionary word that starts at the current index and prepend it to each cached suffix sentence.
# Complexity: Worst-case O(D + n * 2^n) time and O(m + n * 2^n) extra space,
# where n is the string length, D is the total dictionary length, and m is the number of words.

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:

        words = set(wordDict)
        memo = {}

        def dfs(start):

            # reuse the sentences already built for this suffix
            if start in memo:
                return memo[start]

            # empty suffix lets the last word finish the sentence
            if start == len(s):
                return ['']

            result = []

            # for each possible end
            for end in range(start + 1, len(s) + 1):

                word = s[start:end]

                if word in words:
                    # get valid sentences from remaining string
                    sentences = dfs(end)

                    # add a space only when there is a suffix sentence
                    for sentence in sentences:
                        if sentence:
                            result.append(word + ' ' + sentence)
                        else:
                            result.append(word)

            # save answers for this index
            memo[start] = result

            return result

        return dfs(0)
