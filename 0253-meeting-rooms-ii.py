# 253. Meeting Rooms II
# Problem: https://leetcode.com/problems/meeting-rooms-ii/
# Submitted: 2026-10-26 20:41 EDT
# Intuition: Process meetings by start time and reuse the room whose last meeting ends earliest.
# Approach: Keep one end time per allocated room in a min-heap; reuse the earliest free room or allocate another.
# Complexity: O(n log n) time, O(n) space for sorting and the heap.

import heapq

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        
        # sort intervals by start time
        intervals.sort(key=lambda x:x[0])

        # use heap to reuse rooms (no overlap)
        heap = []

        # iterate over sorted intervals
        for start, end in intervals:
            
            # meeting room is free
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            
            # add when this meeting ends
            heapq.heappush(heap, end)

        
        # max meeting rooms being used concurrently
        return len(heap)


