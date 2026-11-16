# 167. Two Sum II - Input Array Is Sorted
# Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Submitted: 2026-11-16 14:46 EST
# Intuition: Sorted values let us shrink the search from either end.
# Approach: Move the right pointer left when the sum is too large and the left
# pointer right when it is too small. Return the matching one-based indices.
# Complexity: O(n) time and O(1) extra space.

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1
