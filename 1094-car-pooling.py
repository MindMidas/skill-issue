# 1094. Car Pooling
# Problem: https://leetcode.com/problems/car-pooling/
# Submitted: 2026-11-13 10:28 EST
# Intuition: The next drop-off determines which passengers can leave before a pickup.
# Approach: Sort trips by pickup location and keep active trips in a min heap keyed by drop-off location. Remove completed trips before adding new passengers and checking capacity.
# Complexity: O(n log n) time and O(n) space for n trips.

import heapq


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        pickup = sorted(trips, key=lambda x: x[1])
        dropoff = []
        curr_capacity = 0

        for c, f, t in pickup:
            # Drop off passengers before picking up the next group.
            while dropoff and dropoff[0][0] <= f:
                _, passengers = heapq.heappop(dropoff)
                curr_capacity -= passengers

            curr_capacity += c
            if curr_capacity > capacity:
                return False
            heapq.heappush(dropoff, (t, c))

        return True
