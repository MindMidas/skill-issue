# 684. Redundant Connection
# Problem: https://leetcode.com/problems/redundant-connection/
# Submitted: 2026-09-05 13:42 EDT
# Intuition: An edge is redundant when its endpoints already have the same root.
# Approach: Use parent pointers to find components and union them until detecting a cycle.
# Complexity: O(n^2) worst-case time, O(n) space; this version has no balancing or path compression.

from collections import deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges)+1)]

        def findRootN(n: int) -> int:
            while parent[n] != n:
                n = parent[n]
            return n

        for a, b in edges:
            root_a = findRootN(a)
            root_b = findRootN(b)

            if root_a == root_b:
                return [a, b]
            
            parent[root_b] = root_a