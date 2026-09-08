# 207. Course Schedule
# Problem: https://leetcode.com/problems/course-schedule/
# Submitted: 2026-09-08 14:56 EDT
# Intuition: All courses are possible exactly when the prerequisite graph has no cycle.
# Approach: DFS with an active path set for cycles and a completed set to reuse results.
# Complexity: O(V + E) time and space.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        visited = set()
        for c, p in prerequisites:
            if c not in graph:
                graph[c] = []
            graph[c].append(p)

        def dfs(c: int, seen: set()) -> bool:
            
            if c in visited:
                return True
            if c not in graph:
                return True
            if c in seen:
                return False

            seen.add(c)

            for p in graph[c]:
                if not dfs(p, seen):
                    return False
            
            seen.remove(c)
            visited.add(c)

            return True
    

        for c in range(numCourses):
            seen = set()
            if not dfs(c, seen):
                return False
        
        return True