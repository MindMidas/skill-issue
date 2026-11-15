# 1807. Evaluate the Bracket Pairs of a String
# Problem: https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
# Submitted: 2026-11-15 13:20 EST
# Intuition: A dictionary gives direct access to each bracketed key's replacement.
# Approach: Copy plain characters and scan each bracketed key through its
# closing parenthesis. Append the matching value or "?", then join the pieces.
# Complexity: O(n + k + r) time with bounded key lengths and O(n + k + r)
# space, where n is the input length, k is the number of entries, and r is
# the output length.


class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        values = {}
        for key, value in knowledge:
            values[key] = value

        result = []
        key = ""
        i = 0

        while i < len(s):
            if s[i] == "(":
                for j in range(i + 1, len(s)):
                    if s[j] == ")":
                        result.append(values.get(key, "?"))
                        key = ""
                        i = j
                        break
                    else:
                        key += s[j]
            else:
                result.append(s[i])

            i += 1

        return "".join(result)
