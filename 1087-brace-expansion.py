# 1087. Brace Expansion
# Problem: https://leetcode.com/problems/brace-expansion/
# Submitted: 2026-11-10 14:10 EST
# Intuition: A literal extends every current prefix, while a brace group branches each prefix into multiple choices.
# Approach: Scan the expression from left to right, expand the current prefixes at each group, and sort the completed words.
# Complexity: O(n + kL^2 + kL log k) time and O(kL) space, where n is the input length, k is the number of words, and L is their length.

class Solution:
    def expand(self, s: str) -> list[str]:

        # helper to process the options
        def processOptions(i):
            options = []

            while s[i] != '}':
                if s[i].isalpha():
                    options.append(s[i])
                i += 1

            return options, i

        result = [""]
        i = 0

        # loop over each char in s
        while i < len(s):

            # we need to process choices
            if s[i] == '{':

                # get choices and new i
                options, i = processOptions(i+1)

                # for each result add each choice and create new_result list
                new_result = []
                for r in result:
                    for o in options:
                        new_result.append(r+o)
                result = new_result

            # just append char to all results
            else:
                for j in range(len(result)):
                    result[j] += s[i]
            i += 1

        # sort for lexicographical order and return
        result.sort()
        return result
