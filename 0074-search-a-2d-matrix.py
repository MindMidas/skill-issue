# 74. Search a 2D Matrix
# Problem: https://leetcode.com/problems/search-a-2d-matrix/
# Submitted: 2026-08-26 14:39 EDT
# Intuition: The matrix's row ordering makes it one sorted array in row-major order.
# Approach: Binary-search a flat index and convert it into a row and column.
# Complexity: O(log(m*n)) time, O(1) space.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = (rows * cols) - 1
        
        while left <= right:

            mid = left + (right - left) // 2
            
            r = mid // cols
            c = mid % cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1


        return False