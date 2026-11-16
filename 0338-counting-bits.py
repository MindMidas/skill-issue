# 338. Counting Bits
# Problem: https://leetcode.com/problems/counting-bits/
# Submitted: 2026-11-16 14:23 EST
# Intuition: Removing the last binary digit leaves a number whose bit count is already known.
# Approach: Add the last bit to the saved count for i // 2.
# Complexity: O(n) time and O(n) space for the result.


class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + (i % 2)

        return ans
