# 1851. Minimum Interval to Include Each Query
# Problem: https://leetcode.com/problems/minimum-interval-to-include-each-query/
# Submitted: 2026-09-02 12:06 EDT
# Intuition: Sorted queries allow intervals to enter a candidate heap only once.
# Approach: Sweep interval starts, discard expired heap entries, and read the smallest length.
# Complexity: O(n log n + q log q + q log(n + 1)) time, O(n + q) space.

import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        heap = []
        sorted_queries = sorted(queries)
        intervals.sort(key=lambda x: x[0])

        answers = {}

        i = 0

        for query in sorted_queries:
 
            while i < len(intervals) and intervals[i][0] <= query:

                left, right = intervals[i]

                if right >= query:
                    heapq.heappush(heap, (right-left+1, right))
                
                i += 1
            
            # remove expired
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            if heap:
                answers[query] = heap[0][0]
            else:
                answers[query] = -1
            
        return [answers[query] for query in queries]




        