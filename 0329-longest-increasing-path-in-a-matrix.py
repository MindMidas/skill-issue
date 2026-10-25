# 329. Longest Increasing Path in a Matrix
# Problem: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Submitted: 2026-10-25 11:57 EDT
# Intuition: The best path from a cell is one plus the best path from any larger neighbor.
# Approach: DFS from every cell and memoize its longest path; strictly increasing moves prevent cycles.
# Complexity: O(m*n) time, O(m*n) space for memoization and the recursion stack.

class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        best_path = {}

        def nextMoves(r,c):

            # possible moves
            moves = [
                (r+1,c), # down
                (r-1,c), # up
                (r,c+1), # right
                (r,c-1)  # left
            ]

            valid = []

            # find valid increasing moves
            for nr, nc in moves:
                if (0 <= nc < cols and 0 <= nr < rows) and matrix[nr][nc] > matrix[r][c]:
                    valid.append((nr,nc))
            
            return valid


        def dfs(r, c):

            # return longest path seen
            if (r,c) in best_path:
                return best_path[(r,c)]

            # explore valid moves and set longest to best one
            longest = 1
            for nr, nc in nextMoves(r,c):
                longest = max(longest, 1 + dfs(nr,nc))
            
            # memorize in dictionary
            best_path[(r,c)] = longest

            return longest


        # for each cell in matrix, find the longest path
        best = 0
        for r in range(rows):
            for c in range(cols):
                best = max(best, dfs(r,c))
        
        return best

        
            

            