# 1381. Design a Stack With Increment Operation
# Problem: https://leetcode.com/problems/design-a-stack-with-increment-operation/
# Submitted: 2026-11-12 12:56 EST
# Intuition: A list gives direct access to the bottom elements while supporting stack operations at the end.
# Approach: Append only while the stack has room. Pop from the end and apply each increment to the first min(k, size) elements.
# Complexity: O(1) amortized time for push and pop, O(min(k, size)) time for increment, and O(maxSize) space.

class CustomStack:
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) != self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
