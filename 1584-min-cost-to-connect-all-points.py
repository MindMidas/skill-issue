# 1584. Min Cost to Connect All Points
# Problem: https://leetcode.com/problems/min-cost-to-connect-all-points/
# Submitted: 2026-09-05 21:21 EDT
# Intuition: Connecting the cheapest edge to a new point grows a minimum spanning tree.
# Approach: Build all Manhattan-distance edges and run Prim's algorithm with a min-heap.
# Complexity: O(n^2 log n) time, O(n^2) space.

import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = {}

        for i in range(len(points)):
            if i not in graph:
                graph[i] = []
            for j in range(len(points)):
                if j == i:
                    continue
                else:
                    graph[i].append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), j))


        visited = set()
        heap = []
        heapq.heappush(heap, (0,0))

        min_cost = 0
        
        while heap:

            c_cost, c_id = heapq.heappop(heap)

            if c_id not in visited:
                visited.add(c_id)
                min_cost += c_cost
            else: 
                continue

            for n_cost, n_id in graph[c_id]:
                if n_id not in visited:
                    heapq.heappush(heap, (n_cost, n_id))

        return min_cost