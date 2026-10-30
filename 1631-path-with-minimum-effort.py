# 1631. Path With Minimum Effort
# Problem: https://leetcode.com/problems/path-with-minimum-effort/
# Submitted: 2026-10-30 12:56 EDT
# Intuition: A path's effort is its largest height difference, so explore the smallest effort first.
# Approach: Use Dijkstra's algorithm with a min heap, updating each neighbor with max(current effort, step difference).
# Complexity: O(mn log(mn)) time, O(mn) extra space, for m rows and n columns.

import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        
        rows = len(heights)
        cols = len(heights[0])

        heap = [(0,0,0)]

        # dict: min effort to reach each cell
        effort = {(0, 0): 0}

        # explore the path with the smallest effort first
        while heap:

            curr_effort, r, c = heapq.heappop(heap)
            
            # skip outdated paths if a better effort was found
            if curr_effort > effort[(r, c)]:
                continue

            # the first valid target popped has minimum effort
            if r == rows - 1 and c == cols - 1:
                return curr_effort
            
            # explore four directions 
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                # valid move check
                if 0 <= nr < rows and  0 <= nc < cols:
                    
                    # path effort is the largest step so far
                    diff = abs(heights[nr][nc] - heights[r][c])
                    new_effort = max(curr_effort, diff)

                    # only push if this improves the cell's best effort
                    if new_effort < effort.get((nr, nc), float('inf')):
                        effort[(nr, nc)] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
