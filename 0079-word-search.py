# 79. Word Search
# Problem: https://leetcode.com/problems/word-search/
# Submitted: 2026-08-31 16:05 EDT
# Intuition: A valid word follows adjacent matching cells without reusing a cell.
# Approach: DFS from each position, tracking the cells in the current path and backtracking.
# Complexity: O(m*n*3^L) time, O(L) space; L is word length.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def validMoves(r,c):

            moves = [
                (r+1, c),
                (r-1, c),
                (r, c+1),
                (r, c-1)
            ]

            valid = []

            for row, col in moves:
                if 0 <= row < len(board) and 0 <= col < len(board[row]):
                    valid.append((row,col))
            
            return valid
        
        def explore(r, c, seen, i) -> bool:
            char = board[r][c]

            if (r,c) in seen:
                return False

            if char == word[i]:
                
                if i == len(word) - 1:
                    return True
                
                seen.add((r,c))
                for nr, nc in validMoves(r,c):
                    if explore(nr, nc, seen, i+1):
                        return True

                seen.remove((r,c))
            
            return False

            
        for r in range(len(board)):
            
            for c, char in enumerate(board[r]):

                if explore(r, c, set(), 0):
                    return True
        
        return False
