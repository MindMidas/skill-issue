# 785. Is Graph Bipartite?
# Problem: https://leetcode.com/problems/is-graph-bipartite/
# Submitted: 2026-11-22 13:07 EST
# Intuition: Every neighbor must belong to the opposite group from its node.
# Approach: Use BFS to assign nodes to two sets, rejecting conflicting edges.
# Start another traversal for each disconnected component.
# Complexity: O(V + E) expected time and O(V) space.

from collections import deque


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        a = set()
        b = set()

        for start in range(len(graph)):
            if start in a or start in b:
                continue

            a.add(start)
            queue = deque([(start, 'b')])
            while queue:
                node, next_group = queue.popleft()
                for neighbor in graph[node]:
                    if ((next_group == 'b' and neighbor in b) or
                            (next_group == 'a' and neighbor in a)):
                        continue

                    if ((next_group == 'b' and neighbor in a) or
                            (next_group == 'a' and neighbor in b)):
                        return False

                    if next_group == 'a':
                        a.add(neighbor)
                    else:
                        b.add(neighbor)
                    queue.append((neighbor, 'b' if next_group == 'a' else 'a'))

        return True
