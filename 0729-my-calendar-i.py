# 729. My Calendar I
# Problem: https://leetcode.com/problems/my-calendar-i/
# Submitted: 2026-11-13 13:11 EST
# Intuition: In a sorted list of disjoint bookings, only the two intervals around the insertion point can overlap a new booking.
# Approach: Find the insertion point with binary search, reject overlaps with either neighbor, and insert the interval if both checks pass.
# Complexity: O(log n) to find the insertion point and O(n) worst-case time to insert into the list, with O(n) space for n bookings.

from bisect import bisect_left


class MyCalendar:
    def __init__(self):
        self.sorted = []

    def book(self, startTime: int, endTime: int) -> bool:
        right = bisect_left(self.sorted, (startTime, endTime))
        left = right - 1

        # Check the right neighbor.
        if right < len(self.sorted) and endTime > self.sorted[right][0]:
            return False

        # Check the left neighbor.
        if left >= 0 and startTime < self.sorted[left][1]:
            return False

        self.sorted.insert(right, (startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
