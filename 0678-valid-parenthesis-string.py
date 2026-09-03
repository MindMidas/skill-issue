# 678. Valid Parenthesis String
# Problem: https://leetcode.com/problems/valid-parenthesis-string/
# Submitted: 2026-09-03 16:10 EDT
# Intuition: Stars can replace brackets only when their positions preserve bracket order.
# Approach: Track opening and star indices; match closing brackets, then remaining openings.
# Complexity: O(n) time, O(n) space.

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        openings = []
        stars = []

        for i, token in enumerate(s):

            if token == "(":
                openings.append(i)
            elif token == ")":
                if openings:
                    openings.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            else:
                stars.append(i)

        while openings:
            if not stars:
                return False
            opening = openings.pop()
            star = stars.pop()

            if star < opening:
                return False
                
        return True