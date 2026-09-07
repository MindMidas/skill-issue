# 62. Unique Paths
# Problem: https://leetcode.com/problems/unique-paths/
# Submitted: 2026-09-07 12:31 EDT
# Intuition: Paths from a cell equal the sum of paths from its down and right neighbors.
# Approach: DFS through valid moves and memoize each cell's path count.
# Complexity: O(m*n) time and space.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        counts = {}

        def getValidMoves(row, col) -> list:
            moves = [(row+1,col), (row, col+1)]
            valid = []

            for move in moves:
                if 0 <= move[0] < m and 0 <= move[1] < n:
                    valid.append(move)

            return valid
        
        def dfs(row, col) -> int:
            
            unique = 0

            if row == m - 1 and col == n - 1:
                return 1
            
            if (row,col) in counts:
                return counts[(row,col)]
            
            for nr, nc in getValidMoves(row, col):
                unique += dfs(nr, nc)
            
            counts[(row,col)] = unique

            return unique

        
        return dfs(0,0)
