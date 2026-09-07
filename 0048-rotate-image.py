# 48. Rotate Image
# Problem: https://leetcode.com/problems/rotate-image/
# Submitted: 2026-09-07 15:50 EDT
# Intuition: A 90-degree rotation cycles four corresponding cells in each layer.
# Approach: Visit each layer and rotate its top, left, bottom, and right cells in place.
# Complexity: O(n^2) time, O(1) space.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for top_row in range(n // 2):
            for top_col in range(top_row, n - 1 - top_row):
                
                # find other cells to swap with 
                right_col = n - 1 - top_row
                right_row = top_col

                bottom_col = n - 1 - top_col
                bottom_row = n - 1 - top_row

                left_col = top_row
                left_row = n - 1 - top_col

                # rotate
                temp_top = matrix[top_row][top_col]

                matrix[top_row][top_col] = matrix[left_row][left_col]
                matrix[left_row][left_col] = matrix[bottom_row][bottom_col]
                matrix[bottom_row][bottom_col] = matrix[right_row][right_col]
                matrix[right_row][right_col] = temp_top

        
