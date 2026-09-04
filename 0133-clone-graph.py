# 133. Clone Graph
# Problem: https://leetcode.com/problems/clone-graph/
# Submitted: 2026-09-03 22:52 EDT
# Intuition: Each original node needs exactly one clone, even when cycles exist.
# Approach: BFS with an original-to-clone map and connect each clone's neighbors.
# Complexity: O(V + E) time and space including the cloned graph.

from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        clone_map = {}
        head = None

        if not node:
            return None
        else:
            clone_map[node] = Node(val=node.val, neighbors=None)
            head = clone_map[node]
            queue = deque([node])
        

        while queue:

            curr = queue.popleft()
            
            for neighbor in curr.neighbors:
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(val=neighbor.val, neighbors=None)
                    queue.append(neighbor)
                
                clone_map[curr].neighbors.append(clone_map[neighbor])

        return head

