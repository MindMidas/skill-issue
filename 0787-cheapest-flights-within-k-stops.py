# 787. Cheapest Flights Within K Stops
# Problem: https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Submitted: 2026-09-06 14:23 EDT
# Intuition: The route state needs both its city and its remaining flight allowance.
# Approach: Use a cost heap and retain improved costs for each (city, remaining) state.
# Complexity: O(E + P log(P + 1)) time, O(E + V*K + P) space; P heap pushes, K = k+1. No stale-entry pruning.

import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = {}
        seen = {}

        for o, d, p in flights:
            if o not in graph:
                graph[o] = []
            graph[o].append((d,p))

        
        heap = []
        heapq.heappush(heap, (0, k+1, src)) # cost so far, remaining flights, city id
        seen[(src, k + 1)] = 0

        while heap:

            cost, remaining, city = heapq.heappop(heap)

            if city == dst:
                return cost
            
            if remaining > 0:
                
                if city in graph:
                    for dst_city, dst_cost in graph[city]:
                        new_cost = cost + dst_cost
                        new_remaining = remaining - 1
                        state = (dst_city, new_remaining)

                        if state not in seen or new_cost < seen[state]:
                            seen[state] = new_cost
                            heapq.heappush(heap, (new_cost, new_remaining, dst_city))
        
        return -1

