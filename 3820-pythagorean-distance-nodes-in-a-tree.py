# 3820. Pythagorean Distance Nodes in a Tree
# Problem: https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/
# Submitted: 2026-11-02 14:00 EST
# Intuition: Precompute distances from the three given nodes, then check each node's distance triple.
# Approach: Run BFS from x, y, and z; sort each triple and count those with a*a + b*b == c*c.
# Complexity: O(n) time, O(n) extra space; a tree has n - 1 edges and each triple has only three values.

from collections import deque
class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:

        # create the graph
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(start):
            
            distances = [-1] * n  # -1 means not visited
            distances[start] = 0  # distance to itself is 0

            # init queue with start
            queue = deque([start])
            
            while queue:
                node = queue.popleft()

                # for each neighbor, if unvisited, update distance and append to queue
                for neighbor in graph[node]:
                    if distances[neighbor] == -1:
                        distances[neighbor] = distances[node] + 1
                        queue.append(neighbor)

            return distances
        
        # get every node's distance from x, y, and z
        dx = bfs(x)
        dy = bfs(y)
        dz = bfs(z)

        # sort each node's three distances so c is the largest
        result = 0
        for i in range(n):
            a,b,c = sorted([dx[i], dy[i], dz[i]])

            # count distances that satisfy the Pythagorean equation
            if (a*a + b*b) == c*c:
                result += 1
        
        return result
