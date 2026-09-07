# 202. Happy Number
# Problem: https://leetcode.com/problems/happy-number/
# Submitted: 2026-09-07 15:59 EDT
# Intuition: Repeated digit-square sums either reach 1 or revisit a previous value.
# Approach: Compute each sum and keep a set of previously seen numbers to detect a cycle.
# Complexity: O(d + t*log(d + 1)) time, O(t) stored values; d initial digits, t subsequent steps.

class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n != 1:
            
            if n in seen:
                return False
            
            seen.add(n)
            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit

                n //= 10

            n = total

        return True