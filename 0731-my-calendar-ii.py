# 731. My Calendar II
# Problem: https://leetcode.com/problems/my-calendar-ii/
# Submitted: 2026-11-14 11:13 EST
# Intuition: A sweep over booking endpoints tracks how many bookings are active.
# Approach: Insert both endpoints, process ends before starts at the same time,
# and remove both new endpoints if the sweep detects a triple booking.
# Complexity: O(n) time per booking and O(n) space for n bookings.

from bisect import insort, bisect_left


class MyCalendarTwo:
    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        insort(self.events, (endTime, -1))
        insort(self.events, (startTime, 1))

        count = 0
        for time, change in self.events:
            count += change

            # Remove both endpoints if this would create a triple booking.
            if count >= 3:
                i = bisect_left(self.events, (startTime, 1))
                self.events.pop(i)
                j = bisect_left(self.events, (endTime, -1))
                self.events.pop(j)
                return False

        return True
