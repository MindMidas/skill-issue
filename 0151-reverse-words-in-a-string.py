# 151. Reverse Words in a String
# Problem: https://leetcode.com/problems/reverse-words-in-a-string/
# Submitted: 2026-11-07 11:23 EST
# Intuition: Reading from right to left naturally puts the words in reverse order.
# Approach: Track each word's boundaries while skipping spaces, then join the collected words.
# Complexity: O(n) time and O(n) space.

class Solution:
    def reverseWords(self, s: str) -> str:

        word = False
        end = None
        start = None
        result = []

        for i in range(len(s)-1, -1, -1):

            # start a word
            if s[i] != ' ' and not word:
                word = True
                end = i

            # a word just ended at a space or the first character
            elif word and (s[i] == ' ' or i == 0):

                if i == 0:
                    if s[i] == ' ':
                        start = i + 1
                    else:
                        start = i
                else:
                    start = i+1

                # add the word
                result.append(s[start:end+1])

                # reset for the next word
                start = None
                end = None
                word = None

        # handle a remaining word
        if word:
            result.append(s[start:end+1])

        return ' '.join(result)
