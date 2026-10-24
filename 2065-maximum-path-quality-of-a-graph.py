# 2065. Maximum Path Quality of a Graph
# Problem: https://leetcode.com/problems/maximum-path-quality-of-a-graph/
# Submitted: 2026-10-24 13:39 EDT
# Intuition: The largest next node may miss a better route, so explore paths with DFS and backtracking.
# Approach: Track time and unique-node scores, backtrack visited nodes, and score routes that return to node 0.
# Complexity: O(V + E + 4^D) time, O(V + E + D) space; D = maxTime // 10, at most 10 edges.

class Solution:

    def maximalPathQuality(self, values: list[int], edges: list[list[int]], maxTime: int) -> int:
        
        graph = [[] for _ in range(len(values))]

        for u, v, t in edges:
            graph[u].append((v,t))
            graph[v].append((u,t))

        visited = {0}

        def dfs(u, time, quality):
            
            best = quality if u == 0 else 0

            for v, t in graph[u]:
                if time + t > maxTime:
                    continue
                
                if v in visited:
                    score = dfs(v, time + t, quality)
                    best = max(best, score)
                else:
                    visited.add(v)

                    score = dfs(v, time + t, quality + values[v])
                    best = max(best, score)

                    visited.remove(v)
            
            return best
        
        return dfs(0, 0, values[0])
