# 20. Valid Parentheses
# Problem: https://leetcode.com/problems/valid-parentheses/
# Submitted: 2026-09-21 14:52 EDT
# Intuition: Each closing bracket must match the most recent unmatched opening bracket.
# Approach: Push openings onto a stack and pop/check for each closing bracket.
# Complexity: O(n) time, O(n) space.

class Solution:
    def isValid(self, s: str) -> bool:
       
        stack = []
        opening = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for b in s:

            if b in opening:
                if stack:
                    if stack.pop() != opening[b]:
                        return False
                else:
                    return False
            else:
                stack.append(b)
            
        if stack:
            return False
        
        return True

