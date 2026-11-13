# 1476. Subrectangle Queries
# Problem: https://leetcode.com/problems/subrectangle-queries/
# Submitted: 2026-11-13 12:51 EST
# Intuition: Updating the grid directly keeps each lookup a single array access.
# Approach: Write the new value to every cell inside the inclusive row and column bounds.
# Complexity: O(h * w) time per update for a region with h rows and w columns, O(1) time per lookup, and O(1) extra space beyond the input grid.

class SubrectangleQueries:
    def __init__(self, rectangle: list[list[int]]):
        self.grid = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                self.grid[r][c] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.grid[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
