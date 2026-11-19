# 371. Sum of Two Integers
# Problem: https://leetcode.com/problems/sum-of-two-integers/
# Submitted: 2026-11-18 19:31 EST
# Intuition: XOR adds without carries, while shifted AND identifies the carries.
# Approach: Repeat XOR and carry propagation with a 32-bit mask, then convert
# the resulting two's-complement representation back to a signed integer.
# Complexity: O(1) time and space for fixed 32-bit integers.


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry

        return a if a <= MAX_INT else ~(a ^ MASK)
