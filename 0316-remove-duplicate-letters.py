# 316. Remove Duplicate Letters
# Problem: https://leetcode.com/problems/remove-duplicate-letters/
# Submitted: 2026-11-04 12:25 EST
# Intuition: Put a smaller letter earlier when the larger letter can still be picked later.
# Approach: Track last indices and use a stack with a set to keep each letter once.
# Complexity: O(n) time, O(1) extra space for the fixed alphabet.

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        added = set()
        last_seen = {}
        stack = []

        # record the last index for each letter
        for i, char in enumerate(s):
            last_seen[char] = i

        for i, char in enumerate(s):

            # skip letters already in the stack
            if char in added:
                continue

            # pop larger letters we can add back later
            while stack and stack[-1] > char and i < last_seen[stack[-1]]:
                popped_char = stack.pop()
                added.remove(popped_char)

            if char not in added:
                stack.append(char)
                added.add(char)

        return ''.join(stack)
