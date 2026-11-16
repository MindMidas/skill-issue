# 547. Number of Provinces
# Problem: https://leetcode.com/problems/number-of-provinces/
# Submitted: 2026-11-16 15:14 EST
# Intuition: Each connected component of cities is one province.
# Approach: Build an adjacency list from the matrix and run DFS from each
# unvisited city, counting one province for every new traversal.
# Complexity: O(n^2) time and O(n^2) space for n cities.

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        g = {i: [] for i in range(n)}

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    g[i].append(j)

        seen = set()
        provinces = 0

        def dfs(node):
            seen.add(node)
            for neighbor in g[node]:
                if neighbor not in seen:
                    dfs(neighbor)

        for node in g:
            if node not in seen:
                dfs(node)
                provinces += 1

        return provinces
