# 417. Pacific Atlantic Water Flow
# Problem: https://leetcode.com/problems/pacific-atlantic-water-flow/
# Submitted: 2026-09-04 13:49 EDT
# Intuition: Reverse water flow from each ocean to find all cells that can reach it.
# Approach: Run uphill BFS from both sets of borders and intersect the visited sets.
# Complexity: O(m*n) time, O(m*n) space.

from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()

        def getValidPrev(row: int, col: int, ocean: str) -> list:
            neighbours = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
            valid = []
            for neighbour in neighbours:
                nr, nc = neighbour
                if 0 <= nr < len(heights) and 0 <= nc < len(heights[nr]):
                    if heights[nr][nc] >= heights[row][col]:
                        if ocean == "pacific":
                            if (nr,nc) not in pacific:
                                pacific.add((nr, nc))
                                valid.append((nr,nc))
                        else:
                            if (nr,nc) not in atlantic:
                                atlantic.add((nr, nc))
                                valid.append((nr,nc))
            return valid
        
        rows = len(heights)
        cols = len(heights[0])

        # init top + bottom rows
        for c in range(cols):
            pacific.add((0, c))
            atlantic.add((rows - 1, c))

        # init left + right columns
        for r in range(rows):
            pacific.add((r, 0))
            atlantic.add((r, cols - 1))

        pq = deque(pacific)
        aq = deque(atlantic)

        while pq:
            for _ in range(len(pq)):
                r, c = pq.popleft()
                for prev in getValidPrev(r, c, "pacific"):
                    pq.append(prev)

        while aq:
            for _ in range(len(aq)):
                r, c = aq.popleft()
                for prev in getValidPrev(r, c, "atlantic"):
                    aq.append(prev)

        both = pacific & atlantic
        return [list(cell) for cell in both]
