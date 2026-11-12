# 722. Remove Comments
# Problem: https://leetcode.com/problems/remove-comments/
# Submitted: 2026-11-12 14:09 EST
# Intuition: A block comment can span lines, so keep both the comment state and the code collected before it.
# Approach: Scan each line, skip block comments through their closing delimiter, and stop at line comments. Emit the buffered code once outside a block comment.
# Complexity: O(n) time and O(n) space, including the output, for n source characters.

class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        result = []
        curr = []
        block = False

        for data in source:
            i = 0

            while i < len(data):
                # Search for the closing delimiter inside a block comment.
                if block:
                    if data[i:i + 2] == "*/":
                        block = False
                        i += 2
                    else:
                        i += 1
                else:
                    if data[i:i + 2] == "/*":
                        block = True
                        i += 2
                    elif data[i:i + 2] == "//":
                        break
                    else:
                        curr.append(data[i])
                        i += 1

            if not block and curr:
                result.append("".join(curr))
                curr = []

        return result
