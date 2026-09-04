# 130. Surrounded Regions
# Problem: https://leetcode.com/problems/surrounded-regions/
# Submitted: 2026-09-04 14:25 EDT
# Intuition: Only O regions connected to a boundary can survive.
# Approach: BFS from boundary O cells, mark them safe, then flip the remaining O cells.
# Complexity: O(m*n) time, O(m*n) space.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def getValidNext(r: int, c: int) -> list:

            moves = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            valid = []

            for move in moves:
                nr, nc = move
                if 0 <= nr < len(board) and 0 <= nc < len(board[nr]) and board[nr][nc] == "O":
                    board[nr][nc] = "V"
                    valid.append(move)
                    
            
            return valid

        queue = deque([])

        for row in range(len(board)):
            if board[row][0] == "O":
                queue.append((row, 0))
                board[row][0] = "V"
            if board[row][len(board[0]) - 1] == "O":
                queue.append((row, len(board[0]) - 1))
                board[row][len(board[0]) - 1] = "V"
        for col in range(1, len(board[0]) - 1):
            if board[0][col] == "O":
                queue.append((0, col))
                board[0][col] = "V"
            if board[len(board) - 1][col] == "O":
                queue.append((len(board) - 1, col))
                board[len(board) - 1][col] = "V"
    

        while queue:

            for _ in range(len(queue)):

                row, col = queue.popleft()

                for move in getValidNext(row,col):
                    queue.append(move)

        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == "O":
                    board[r][c] = "X"
                elif val == "V":
                    board[r][c] = "O"
        return