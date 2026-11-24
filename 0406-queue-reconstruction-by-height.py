# 406. Queue Reconstruction by Height
# Problem: https://leetcode.com/problems/queue-reconstruction-by-height/
# Submitted: 2026-11-24 16:55 EST
# Intuition: Placing taller people first lets each k specify an insertion index.
# Approach: Sort by descending height and ascending k, then insert each person
# at index k so exactly k people of at least their height precede them.
# Complexity: O(n^2) time and O(n) space.


class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue
