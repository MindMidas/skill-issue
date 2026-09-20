# 68. Text Justification
# Problem: https://leetcode.com/problems/text-justification/
# Submitted: 2026-09-20 14:52 EDT
# Intuition: Pack each line greedily, assigning extra spaces to its leftmost gaps.
# Approach: Track the current words, distribute spaces when full, and left-align the last line.
# Complexity: O(n + l*w^2) worst-case time from string concatenation, O(n + l*w) space; l lines, width w.

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        
        solution = []
        curr_len = 0
        curr_spaces = 0
        curr_words = []
        curr_solution = ""


        for i, word in enumerate(words):
            
            curr_width = curr_len + curr_spaces

            # check if word can be added to curr line
            if curr_width + len(word) + (1 if curr_words else 0) <= maxWidth:
                curr_words.append(i)
                curr_len += len(word) 

                if len(curr_words) > 1:
                    curr_spaces += 1

            # we can't add the word so complete line and start new
            else:
                
                curr_spaces += maxWidth - curr_width

                if len(curr_words) == 1:
                    curr_solution += words[curr_words[0]]
                    curr_solution += " " * (maxWidth - len(curr_solution))
                else:
                    spaces_per_gap = curr_spaces // (len(curr_words) - 1)
                    extra_spaces = curr_spaces % (len(curr_words) - 1)

                    for j, w in enumerate(curr_words):
                        curr_solution += words[w]

                        if j < len(curr_words) - 1:
                            curr_solution += " " * spaces_per_gap

                            if j < extra_spaces:
                                curr_solution += " "

                solution.append(curr_solution)
                
                curr_len = 0
                curr_spaces = 0
                curr_words = []
                curr_solution = ""

                # process curr word
                curr_words.append(i)
                curr_len += len(word)


        # process last line
        for j, w in enumerate(curr_words):

            curr_solution += words[w]
            
            if j == len(curr_words) - 1:
                curr_solution += " " * (maxWidth - len(curr_solution))
            else:
                curr_solution += " "
        
        solution.append(curr_solution)

        return solution