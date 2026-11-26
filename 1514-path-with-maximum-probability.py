# 1514. Path with Maximum Probability
# Problem: https://leetcode.com/problems/path-with-maximum-probability/
# Submitted: 2026-11-26 10:33 EST
# Intuition: Explore the highest-probability path first using modified Dijkstra.
# Approach: Build an undirected graph and use a max-heap with negated
# probabilities, updating neighbors only when their probability improves.
# Complexity: O((V + E) log(V + E)) time and O(V + E) space.

import heapq


class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        g = [[] for _ in range(n)]
        for (a, b), p in zip(edges, succProb):
            g[a].append((b, p))
            g[b].append((a, p))

        best = [0.0] * n
        best[start_node] = 1.0
        max_heap = [(-1.0, start_node)]

        while max_heap:
            p, node = heapq.heappop(max_heap)
            p = -p
            if p < best[node]:
                continue
            if node == end_node:
                return p

            for new_node, edge_p in g[node]:
                new_p = p * edge_p
                if new_p > best[new_node]:
                    best[new_node] = new_p
                    heapq.heappush(max_heap, (-new_p, new_node))

        return 0.0
