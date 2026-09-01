# 621. Task Scheduler
# Problem: https://leetcode.com/problems/task-scheduler/
# Submitted: 2026-09-01 15:04 EDT
# Intuition: Run the most frequent available task while cooling down recently used tasks.
# Approach: Simulate each time slot with a max-heap of counts and a cooldown queue.
# Complexity: O(N + t log(a + 1)) time, O(a) space; t simulated slots, a distinct tasks.

import heapq
from collections import deque

class Solution:
    def getFrequency(self, tasks: List[str]) -> dict:
        freq = {}
        
        for task in tasks:
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1

        return freq

    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = self.getFrequency(tasks)
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)
        cooldown = deque([])

        i = 0

        while heap or cooldown:
            
            while cooldown and cooldown[0][1] <= i:
                heapq.heappush(heap, cooldown.popleft()[0])
            if heap:
                task = heapq.heappop(heap) + 1
                if task < 0:
                    cooldown.append((task, i+n+1))

            i += 1

        return i