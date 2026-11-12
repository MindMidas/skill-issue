# 933. Number of Recent Calls
# Problem: https://leetcode.com/problems/number-of-recent-calls/
# Submitted: 2026-11-12 12:34 EST
# Intuition: Ping timestamps arrive in increasing order, so expired pings are always at the front of the queue.
# Approach: Append the new timestamp and remove entries strictly before t - 3000. The remaining queue length is the count in the inclusive window.
# Complexity: O(1) amortized time per ping since each timestamp is appended and removed at most once. Space is O(w) for the maximum number of pings in the window.

from collections import deque


class RecentCounter:
    def __init__(self):
        self.pings = deque()

    def ping(self, t: int) -> int:
        self.pings.append(t)

        # pop invalid pings
        while self.pings and self.pings[0] < t - 3000:
            self.pings.popleft()

        return len(self.pings)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
