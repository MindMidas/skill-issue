# 1254. Number of Closed Islands
# Problem: https://leetcode.com/problems/number-of-closed-islands/
# Submitted: 2026-11-06 12:42 EST
# Intuition: A land component is closed exactly when none of its cells touches the grid border.
# Approach: DFS each unvisited land component, mark its cells, and propagate whether any cell touches a border.
# Complexity: O(mn) time and O(mn) recursion space.

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        closed_islands = 0

        def getValidNext(r, c):

            # next possible moves/cells
            moves = [
                (r+1,c),
                (r-1,c),
                (r,c+1),
                (r,c-1)
            ]

            result = []

            # check if this cell touches border
            invalid = (r == 0 or r == rows - 1 or c == 0 or c == cols - 1)

            # mark this cell as visited
            grid[r][c] = -1

            for nr, nc in moves:

                # valid and unvisited
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    result.append((nr,nc))

            return result, invalid

        def dfs(r,c):

            # get next moves and validity
            moves, invalid = getValidNext(r,c)

            # recurse for each move
            for nr, nc in moves:
                if grid[nr][nc] == 0 and dfs(nr,nc):
                    invalid = True

            return invalid

        # call dfs on starting cell of each island
        for r in range(rows):
            for c in range(cols):

                # only increment count if valid
                if grid[r][c] == 0 and not dfs(r,c):
                    closed_islands += 1

        return closed_islands
