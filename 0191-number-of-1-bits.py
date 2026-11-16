# 191. Number of 1 Bits
# Problem: https://leetcode.com/problems/number-of-1-bits/
# Submitted: 2026-11-16 14:37 EST
# Intuition: The remainder after dividing by two is the last binary digit.
# Approach: Count each remainder and divide n by two until it becomes zero.
# Complexity: O(log(n + 1)) time and O(1) space.


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            count += n % 2
            n //= 2

        return count
