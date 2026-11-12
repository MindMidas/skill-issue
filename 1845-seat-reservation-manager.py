# 1845. Seat Reservation Manager
# Problem: https://leetcode.com/problems/seat-reservation-manager/
# Submitted: 2026-11-12 13:35 EST
# Intuition: A min heap keeps the smallest available seat at the top.
# Approach: Heapify all seat numbers, pop the smallest on reservation, and push released seats back onto the heap.
# Complexity: O(n) initialization and space, with O(log n) time per reserve or unreserve.

import heapq


class SeatManager:
    def __init__(self, n: int):
        self.unreserved = [i for i in range(1, n + 1)]
        heapq.heapify(self.unreserved)

    def reserve(self) -> int:
        return heapq.heappop(self.unreserved)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreserved, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
