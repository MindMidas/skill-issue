# 2938. Separate Black and White Balls
# Problem: https://leetcode.com/problems/separate-black-and-white-balls/
# Submitted: 2026-11-04 11:42 EST
# Intuition: Every black ball before a white ball must swap past it once.
# Approach: Scan left to right and add the number of ones seen so far whenever we find a zero.
# Complexity: O(n) time, O(1) extra space.

class Solution:
    def minimumSteps(self, s: str) -> int:

        counter = 0
        swaps = 0

        # read left to right
        for ball in s:

            # each zero has to cross every one seen so far
            if ball == '1':
                counter += 1
            else:
                swaps += counter

        return swaps
