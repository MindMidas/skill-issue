# 695. Max Area of Island
# Problem: https://leetcode.com/problems/max-area-of-island/
# Submitted: 2026-09-03 17:12 EDT
# Intuition: An island's area is the number of land cells reachable from any one of them.
# Approach: BFS each unvisited island, marking land in place and counting its cells.
# Complexity: O(m*n) time, O(m*n) space.

from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def validMoves(row: int, col: int) -> list:
            moves = [(row+1,col), (row-1,col), (row,col+1), (row,col-1)]
            valid = []
            for move in moves:
                nr, nc = move
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] == 1:
                        valid.append(move)
            return valid
        
        queue = deque([])
        best_area = 0
        curr_area = 0

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):

                if cell == 1:
                    grid[r][c] = -1
                    queue.append((r,c))
                    curr_area = 1

                    while queue:
                        pr, pc = queue.popleft()

                        for move in validMoves(pr, pc):
                            queue.append(move)
                            nr, nc = move
                            grid[nr][nc] = -1
                            curr_area += 1
                        
                    best_area = max(curr_area, best_area)

        return best_area 