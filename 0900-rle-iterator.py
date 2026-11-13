# 900. RLE Iterator
# Problem: https://leetcode.com/problems/rle-iterator/
# Submitted: 2026-11-13 12:41 EST
# Intuition: An entire run can be consumed at once using its remaining count.
# Approach: Track the current run, skip runs that are too short, and subtract the remaining request from the run that contains the final element.
# Complexity: O(1 + k) time per call that advances past k runs. O(1) extra space because remaining counts are stored in the input encoding.

class RLEIterator:
    def __init__(self, encoding: list[int]):
        self.encoding = encoding
        self.curr = 0

    def next(self, n: int) -> int:
        last = -1
        consumed = 0

        while consumed < n and self.curr < len(self.encoding):
            available = self.encoding[self.curr]
            needed = n - consumed

            if available >= needed:
                self.encoding[self.curr] -= needed
                return self.encoding[self.curr + 1]

            consumed += available
            self.curr += 2

        return last


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
