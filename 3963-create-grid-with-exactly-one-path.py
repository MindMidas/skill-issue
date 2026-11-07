# 3963. Create Grid With Exactly One Path
# Problem: https://leetcode.com/problems/create-grid-with-exactly-one-path/
# Submitted: 2026-11-06 19:45 EST
# Intuition: Leaving only the top row and last column open forces a single route.
# Approach: Create an open top row, then block every cell except the last column in each remaining row.
# Complexity: O(mn) time and O(mn) output space.

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        grid = ['.' * n]

        for row in range(1, m):
            grid.append('#' * (n - 1) + '.')

        return grid
