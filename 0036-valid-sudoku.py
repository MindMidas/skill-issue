# 36. Valid Sudoku
# Problem: https://leetcode.com/problems/valid-sudoku/
# Submitted: 2026-08-11 18:26 EDT
# Intuition: Each nonempty digit must appear only once in its row, column, and 3-by-3 box.
# Approach: Track three sets of seen digits and reject any repeated entry.
# Complexity: O(1) time and space for the fixed 9-by-9 board.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):

                val = board[row][col]
                if val == ".":
                    continue
                
                # check rows
                if val in rows[row]:
                    return False
                # check cols
                if val in cols[col]:
                    return False
                # check sub boxes
                box_row = row // 3
                box_col = col // 3
                box_index = box_row * 3 + box_col

                if val in boxs[box_index]:
                    return False
                
                # add vals
                rows[row].add(val)
                cols[col].add(val)
                boxs[box_index].add(val)

        return True