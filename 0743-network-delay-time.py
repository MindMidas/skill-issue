# 743. Network Delay Time
# Problem: https://leetcode.com/problems/network-delay-time/
# Submitted: 2026-09-05 15:26 EDT
# Intuition: The signal reaches each node along its cheapest path from the source.
# Approach: Run Dijkstra with a heap and return the largest distance, or -1 if unreachable.
# Complexity: O(V + E log(E + 1)) time, O(V + E) space.

import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        min_time = [float("inf") for _ in range(n + 1)]
        min_time[k] = 0

        graph = {}

        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v,w))

        heap = []
        heapq.heappush(heap, (0, k))

        while heap:

            uw, u = heapq.heappop(heap)

            if uw > min_time[u]:
                continue
            
            if u in graph:
                for v, vw in graph[u]:
                    
                    nw = uw + vw

                    if nw < min_time[v]:
                        min_time[v] = nw
                        heapq.heappush(heap,(nw, v))
    
        for i in range(1, n + 1):
            if min_time[i] == float("inf"):
                return  -1
        
        return max(min_time[1:])