# 155. Min Stack
# Problem: https://leetcode.com/problems/min-stack/
# Submitted: 2026-08-12 13:34 EDT
# Intuition: Every stack entry can remember the minimum among itself and all entries below.
# Approach: Store each value alongside the running minimum to answer every operation directly.
# Complexity: O(1) amortized time per operation, O(n) space.

class MinStack:

    def __init__(self):
        self.stack = [];

    def push(self, value: int) -> None:
        curr_min = value;
        if self.stack:
            curr_min = self.stack[-1][1];
        self.stack.append((value, min(value, curr_min)));

    def pop(self) -> None:
        self.stack.pop();

    def top(self) -> int:
        return self.stack[-1][0];

    def getMin(self) -> int:
        return self.stack[-1][1];


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()