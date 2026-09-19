# 73. Set Matrix Zeroes
# Problem: https://leetcode.com/problems/set-matrix-zeroes/
# Submitted: 2026-09-19 13:46 EDT
# Intuition: Every original zero determines a complete row and column to clear.
# Approach: Record zero rows and columns in sets, then update the matrix in a second pass.
# Complexity: O(m*n) time, O(m + n) space.

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        zero_rows = set()
        zero_cols = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0