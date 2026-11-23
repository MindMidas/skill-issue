# 904. Fruit Into Baskets
# Problem: https://leetcode.com/problems/fruit-into-baskets/
# Submitted: 2026-11-23 10:36 EST
# Intuition: Find the longest contiguous window containing at most two fruit types.
# Approach: Maintain window frequencies, shrinking from the left when a third
# type appears, and track the longest valid window.
# Complexity: O(n) expected time and O(1) extra space.

from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        freq = defaultdict(int)
        left = 0
        max_fruits = 0
        for right in range(len(fruits)):
            freq[fruits[right]] += 1
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
