# 934. Shortest Bridge
# Problem: https://leetcode.com/problems/shortest-bridge/
# Submitted: 2026-11-24 11:17 EST
# Intuition: Expand from one island until reaching the other, crossing the least water.
# Approach: Mark the first island with DFS, then run BFS from all its cells
# and count water cells crossed before reaching the second island.
# Complexity: O(n^2) time and space for an n by n grid.

from collections import deque


class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def validMoves(r, c, types):
            moves = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            valid = []
            for nr, nc in moves:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] in types:
                    valid.append((nr, nc))
            return valid

        island = set()

        def exploreIsland(r, c):
            for nr, nc in validMoves(r, c, {1}):
                if (nr, nc) not in island:
                    island.add((nr, nc))
                    exploreIsland(nr, nc)

        for r in range(rows):
            if island:
                break
            for c in range(cols):
                if grid[r][c] == 1:
                    island.add((r, c))
                    exploreIsland(r, c)
                    break

        seen = set()
        queue = deque([((r, c), 0) for r, c in island])
        seen = island
        while queue:
            (r, c), total = queue.popleft()
            for nr, nc in validMoves(r, c, {1, 0}):
                if (nr, nc) not in seen:
                    if grid[nr][nc] == 1:
                        return total
                    else:
                        seen.add((nr, nc))
                        queue.append(((nr, nc), total + 1))
