# 1823. Find the Winner of the Circular Game
# Problem: https://leetcode.com/problems/find-the-winner-of-the-circular-game/
# Submitted: 2026-10-30 13:16 EDT
# My intuition: Simulate the game rules, keeping the remaining players in O(n) space.
# Follow-up: I learned the O(1) space recurrence below; I didn't come up with it myself.
# Approach: Start with the winner for one player, then shift by k modulo each larger circle size.
# Complexity: O(n) time, O(1) extra space for the submitted follow-up.

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        # with 1 player, the winner is at index 0
        winner = 0

        # build up from 2 players to n players
        for i in range(2, n + 1):

            # shift previous winner by k pos
            # mod handles wrapping around circle
            winner = (winner + k) % i

        # convert from 0-indexed to 1-indexed
        return winner + 1
