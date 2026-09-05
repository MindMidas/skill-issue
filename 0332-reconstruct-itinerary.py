# 332. Reconstruct Itinerary
# Problem: https://leetcode.com/problems/reconstruct-itinerary/
# Submitted: 2026-09-05 16:04 EDT
# Intuition: Using every ticket forms an Eulerian trail; postorder handles dead ends.
# Approach: Reverse-sort destinations, consume the smallest first, and prepend completed airports.
# Complexity: O(E log E) time, O(E) space.

from collections import deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = {}
        path = deque([])

        for o, d in tickets:
            if o not in graph:
                graph[o] = []
            graph[o].append(d)

        for o in graph:
            graph[o].sort(reverse=True)

        def dfs(o: str):

            while o in graph and graph[o]:
                dfs(graph[o].pop())
            
            path.appendleft(o)


        dfs("JFK")
        
        return list(path)


