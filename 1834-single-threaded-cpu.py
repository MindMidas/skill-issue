# 1834. Single-Threaded CPU
# Problem: https://leetcode.com/problems/single-threaded-cpu/
# Submitted: 2026-11-20 19:05 EST
# Intuition: A min-heap ranks available tasks by processing time and original index.
# Approach: Sort tasks by enqueue time, add available tasks to the heap, and
# process its minimum. Jump to the next enqueue time when the CPU is idle.
# Complexity: O(n log n) time and O(n) space.

import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        records = sorted((start, duration, i) for i, (start, duration) in enumerate(tasks))
        heap = []
        curr_time = 0
        i = 0
        results = []

        while len(results) < len(records):
            if not heap and i < len(records):
                curr_time = max(curr_time, records[i][0])

            while i < len(records) and records[i][0] <= curr_time:
                start, duration, index = records[i]
                heapq.heappush(heap, (duration, index))
                i += 1

            if heap:
                duration, index = heapq.heappop(heap)
                results.append(index)
                curr_time += duration

        return results
