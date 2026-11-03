# 402. Remove K Digits
# Problem: https://leetcode.com/problems/remove-k-digits/
# Submitted: 2026-11-03 17:39 EST
# Intuition: Smaller digits matter most near the front, so remove a larger previous digit when a smaller one arrives.
# Approach: Use a monotonic stack while removals remain, trim any leftover removals from the end, and strip leading zeros.
# Complexity: O(n) time, O(n) extra space; each digit is pushed once and popped at most once.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []

        for n in num:
            
            # remove larger previous digits to make the earliest possible position smaller
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -= 1
            
            # add digit to stack
            stack.append(n)
        
        # if removals remain, drop the largest trailing digits
        if k > 0:
            stack = stack[:-k]
        
        # convert to string and remove leading zeros
        solution = ''.join(stack).lstrip('0')

        return solution if solution else '0'
