# 6. Zigzag Conversion
# Problem: https://leetcode.com/problems/zigzag-conversion/
# Submitted: 2026-09-19 13:08 EDT
# Intuition: Characters bounce between the first and last rows of the zigzag.
# Approach: Accumulate row strings while changing direction at the boundaries, then join rows.
# Complexity: O(n^2 + r) worst-case time from string concatenation, O(n) space; r = numRows.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        rows = {}
        curr_row = 0
        direction = -1

        if numRows == 1:
            return s
            
        for char in s:

            if curr_row not in rows:
                rows[curr_row] = ""
            
            rows[curr_row] += char

            if (curr_row == numRows-1) and direction == -1:
                direction = 1
                curr_row -= 1
            elif curr_row == 0 and direction == 1:
                direction = -1
                curr_row += 1
            elif direction == -1:
                curr_row += 1
            else:
                curr_row -= 1

        solution = ""
        for row in range(numRows):

            if row in rows:
                solution += rows[row]
        
        return solution

