# 227. Basic Calculator II
# Problem: https://leetcode.com/problems/basic-calculator-ii/
# Submitted: 2026-11-07 12:59 EST
# Intuition: Store addition and subtraction terms, but immediately fold multiplication and division into the previous term.
# Approach: Build each number while scanning the expression, apply the last operator when the next operator or end is reached, then sum the stack.
# Complexity: O(n) time and O(n) space.

class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        num = ""
        operation = "+"

        for i, c in enumerate(s):
            # build the current number
            if c.isdigit():
                num += c

            # process the number at an operator or the end of the string
            if c in "+-*/" or i == len(s) - 1:

                if operation == "+":
                    stack.append(int(num))
                elif operation == "-":
                    stack.append(-int(num))
                elif operation == "*":
                    stack.append(stack.pop() * int(num))
                else:
                    stack.append(int(stack.pop() / int(num)))

                num = ""
                operation = c

        return sum(stack)
