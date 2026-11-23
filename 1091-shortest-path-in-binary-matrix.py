# 1091. Shortest Path in Binary Matrix
# Problem: https://leetcode.com/problems/shortest-path-in-binary-matrix/
# Submitted: 2026-11-23 13:33 EST
# Intuition: BFS finds the shortest path when each step has equal cost.
# Approach: Explore all eight neighboring clear cells, tracking visited
# positions and path length. Reject blocked endpoints or an unreachable target.
# Complexity: O(n^2) time and space for an n by n grid.

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        def validMoves(r, c):
            moves = [
                (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1),
                (r + 1, c + 1), (r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1)
            ]
            valid = []
            for nr, nc in moves:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    valid.append((nr, nc))
            return valid

        queue = deque([((0, 0), 1)])
        visited = {(0, 0)}
        while queue:
            (r, c), l = queue.popleft()
            if r == rows - 1 and c == cols - 1:
                return l
            for nr, nc in validMoves(r, c):
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), l + 1))

        return -1
