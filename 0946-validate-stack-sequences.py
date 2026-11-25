# 946. Validate Stack Sequences
# Problem: https://leetcode.com/problems/validate-stack-sequences/
# Submitted: 2026-11-25 14:19 EST
# Intuition: Pop a value as soon as the stack top matches the next required value.
# Approach: Simulate pushes in order and all immediately possible pops, then
# check whether the stack is empty.
# Complexity: O(n) time and O(n) space.


class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        j = 0
        for num in pushed:
            stack.append(num)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return not stack
