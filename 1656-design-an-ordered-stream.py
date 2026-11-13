# 1656. Design an Ordered Stream
# Problem: https://leetcode.com/problems/design-an-ordered-stream/
# Submitted: 2026-11-13 12:03 EST
# Intuition: A pointer tracks the earliest value that has yet to be emitted.
# Approach: Store values at their ID positions, then collect the contiguous filled entries starting at the pointer.
# Complexity: O(n) initialization time and space, with O(1 + k) time per insertion that emits k values.

class OrderedStream:
    def __init__(self, n: int):
        self.data = [""] * n
        self.next = 0

    def insert(self, idKey: int, value: str) -> list[str]:
        self.data[idKey - 1] = value
        result = []

        while self.next < len(self.data) and self.data[self.next] != "":
            result.append(self.data[self.next])
            self.next += 1

        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
