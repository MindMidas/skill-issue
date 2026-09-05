# 210. Course Schedule II
# Problem: https://leetcode.com/problems/course-schedule-ii/
# Submitted: 2026-09-05 12:45 EDT
# Intuition: Courses with no remaining prerequisites can be taken next.
# Approach: Run Kahn's topological sort with indegrees and a queue.
# Complexity: O(V + E) time and space.

from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        queue = deque([])
        order = []

        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
        
        indegree = [0] * numCourses

        for courses in graph:
            for course in courses:
                indegree[course] += 1
        
        for course, prereqs in enumerate(indegree):
            if prereqs == 0:
                queue.append(course)

        while queue:
            prereq = queue.popleft()
            order.append(prereq)

            for course in graph[prereq]:
                indegree[course] -= 1
                
                if indegree[course] == 0:
                    queue.append(course)
        
    
        
        return order if len(order) == numCourses else []