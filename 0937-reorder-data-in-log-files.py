# 937. Reorder Data in Log Files
# Problem: https://leetcode.com/problems/reorder-data-in-log-files/
# Submitted: 2026-11-11 14:26 EST
# Intuition: Letter logs need sorting by content and identifier, while digit logs retain their original order.
# Approach: Split logs into content and identifier pairs. Sort the letter pairs, append the digit pairs, and reconstruct the strings.
# Complexity: O(L + m log m * w) time and O(L) space, where L is total input length, m is the number of letter logs, and w is the maximum log length.

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        result = []
        digit_logs = []

        for log in logs:
            data = log.split(" ")
            identifier = data[0]
            content = data[1:]

            if data[1].isdigit():
                digit_logs.append((content, identifier))
            else:
                result.append((content, identifier))

        result.sort()
        result.extend(digit_logs)

        for i, (content, identifier) in enumerate(result):
            result[i] = identifier + " " + " ".join(content)

        return result
