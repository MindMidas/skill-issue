# 2080. Range Frequency Queries
# Problem: https://leetcode.com/problems/range-frequency-queries/
# Submitted: 2026-11-14 14:38 EST
# Intuition: Store each value's occurrence indices in sorted order.
# Approach: Use two binary searches to find the first index at or after left
# and the first index after right. Their positions differ by the range frequency.
# Complexity: O(n) build time and space, with O(log(m + 1)) time per query
# for a value with m occurrences when m > 0, and O(1) for a missing value.

from bisect import bisect_left, bisect_right


class RangeFreqQuery:
    def __init__(self, arr: list[int]):
        self.seen_at = {}

        for i, n in enumerate(arr):
            if n not in self.seen_at:
                self.seen_at[n] = []
            self.seen_at[n].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.seen_at:
            return 0

        indices = self.seen_at[value]
        freq = bisect_right(indices, right) - bisect_left(indices, left)
        return freq
