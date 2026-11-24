# 658. Find K Closest Elements
# Problem: https://leetcode.com/problems/find-k-closest-elements/
# Submitted: 2026-11-24 15:38 EST
# Intuition: The closest elements form a contiguous window around x's insertion point.
# Approach: Find that point with binary search, then expand toward the closer
# neighbor until k elements are selected, preferring the left on ties.
# Complexity: O(log n + k) time and O(k) output space.

from bisect import bisect_left
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        index = bisect_left(arr, x)
        left = index - 1
        right = index

        while right - left - 1 < k:
            if left < 0:
                right += 1
            elif right >= n:
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        return arr[left + 1:right]
