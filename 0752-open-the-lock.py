# 752. Open the Lock
# Problem: https://leetcode.com/problems/open-the-lock/
# Submitted: 2026-11-18 12:16 EST
# Intuition: Each lock combination is a graph node, and one wheel turn is an edge.
# Approach: Use BFS from "0000", skipping deadends and visited combinations.
# Complexity: O(d + 10^4) time and space for d deadends and a four-wheel lock.

from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        def rotate(lock: str):
            moves = []
            for i, wheel in enumerate(lock):
                wheel = int(wheel)
                forward = (wheel + 1) % 10
                backward = (wheel - 1) % 10
                moves.append(lock[:i] + str(forward) + lock[i + 1:])
                moves.append(lock[:i] + str(backward) + lock[i + 1:])
            return moves

        queue = deque([("0000", 0)])
        dead = set(deadends)
        seen = {"0000"}
        if "0000" in dead:
            return -1

        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns

            for next_lock in rotate(lock):
                if next_lock not in seen and next_lock not in dead:
                    queue.append((next_lock, turns + 1))
                    seen.add(next_lock)

        return -1
