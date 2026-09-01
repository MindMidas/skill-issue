# 51. N-Queens
# Problem: https://leetcode.com/problems/n-queens/
# Submitted: 2026-08-31 20:48 EDT
# Intuition: One queen per row is safe when its column and diagonals are unused.
# Approach: Backtrack by row while tracking attacked columns and diagonals in sets.
# Complexity: O(n*n! + s*n^2) time, O(n^2 + s*n^2) space; s output boards.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        answers = []
        cols = set()
        diag1 = set()
        diag2 = set()

        def createBoard(n):
            board = []
            for r in range(n):
                board.append([])
                for c in range(n):
                    board[r].append('.')
            return board
    
        def isValidPosition(row, col):
            if col in cols:
                return False
            if row - col in diag1:
                return False
            if row + col in diag2:
                return False
            return True
        
        def addAttack(row, col):
            cols.add(col)
            diag1.add(row-col)
            diag2.add(row+col)
        def removeAttack(row, col):
            cols.remove(col)
            diag1.remove(row-col)
            diag2.remove(row+col)

        def explore(row):

            if row == n:
                answers.append(["".join(r) for r in board])
                return
            
            for col in range(n):

                if isValidPosition(row, col):
                    board[row][col] = 'Q'
                    addAttack(row,col)
                    explore(row+1)
                    board[row][col] = '.'
                    removeAttack(row,col)
        
        board = createBoard(n)
        explore(0)
        return answers

       
        
        
        