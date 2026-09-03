# 200. Number of Islands
# Problem: https://leetcode.com/problems/number-of-islands/
# Submitted: 2026-09-03 16:52 EDT
# Intuition: Each unvisited land cell starts a new connected component.
# Approach: Scan the grid and BFS each island, marking its land as visited in place.
# Complexity: O(m*n) time, O(m*n) space.

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def getNextMoves(i,j) -> list:
            moves = [
                (i+1,j),
                (i-1,j),
                (i,j+1),
                (i,j-1)
            ]

            valid = []
            for move in moves:
                if (0 <= move[0] < len(grid)) and (0 <= move[1] < len(grid[0])):
                    if grid[move[0]][move[1]] == "1":
                        valid.append(move) 
            
            return valid
    
        num_islands = 0

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
            
                if cell == "1":
                    num_islands += 1

                    queue = deque([(r, c)])
                    grid[r][c] = "-1"

                    while queue:
                        
                        i, j = queue.popleft()

                        for move in getNextMoves(i, j):
                            grid[move[0]][move[1]] = "-1"
                            queue.append(move)

            
        return num_islands