# 994. Rotting Oranges
# Problem: https://leetcode.com/problems/rotting-oranges/
# Submitted: 2026-09-04 12:51 EDT
# Intuition: All currently rotten oranges spread simultaneously each minute.
# Approach: Use multi-source BFS in layers and track the remaining fresh oranges.
# Complexity: O(m*n) time, O(m*n) space.

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def getNextOranges(row, col) -> list:

            neighbours = [(row+1,col), (row-1,col), (row,col+1), (row,col-1)] 
            valid = []

            for neighbour in neighbours:
                nr, nc = neighbour
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]):
                    if grid[nr][nc] == 1:
                        valid.append((nr,nc))

            return valid

        total_mins = 0
        queue = deque([])
        remaining_fresh = 0

        for r, row in enumerate(grid):
            for c, orange in enumerate(row):
                if orange == 2:
                    queue.append((r,c))
                elif orange == 1:
                    remaining_fresh += 1

        
        while queue and remaining_fresh > 0:
            
            for _ in range(len(queue)):
                
                row, col = queue.popleft()

                for nr, nc in getNextOranges(row, col):
                    queue.append((nr, nc))
                    grid[nr][nc] = 2
                    remaining_fresh -= 1

            total_mins += 1
        
        return -1 if remaining_fresh != 0 else total_mins


