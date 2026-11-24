# 901. Online Stock Span
# Problem: https://leetcode.com/problems/online-stock-span/
# Submitted: 2026-11-24 11:36 EST
# Intuition: A decreasing stack can summarize spans of prices no larger than today's.
# Approach: Pop all prices at most the current price, accumulate their spans,
# and push the current price with the combined span.
# Complexity: O(1) amortized time per next call and O(n) space after n calls.


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _, prev_span = self.stack.pop()
            span += prev_span
        self.stack.append((price, span))
        return span
