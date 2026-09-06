# 778. Swim in Rising Water
# Problem: https://leetcode.com/problems/swim-in-rising-water/
# Submitted: 2026-09-06 13:19 EDT
# Intuition: A path becomes usable when the water reaches its highest elevation.
# Approach: Use a min-heap to expand the smallest path maximum and finalize each cell once.
# Complexity: O(n^2 log n) time, O(n^2) space for an n-by-n grid.

import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        def getValidMoves(r, c) -> list:
            moves = [(r+1,c), (r-1,c), (r, c+1), (r, c-1)]
            valid = []
            for nr,nc in moves:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]):
                    valid.append((nr,nc))
            return valid

        heap = []
        visited = set()
        heapq.heappush(heap, (grid[0][0], (0,0)))

        while heap:

            time, (row,col) = heapq.heappop(heap)

            if (row,col) not in visited:
                visited.add((row,col))
            else:
                continue
            
            if row == len(grid) - 1 and col == len(grid[row]) - 1:
                return time
            
            for nr, nc in getValidMoves(row, col):

                if (nr, nc) not in visited:
                    heapq.heappush(heap, (max(time, grid[nr][nc]), (nr,nc)))