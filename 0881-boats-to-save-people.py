# 881. Boats to Save People
# Problem: https://leetcode.com/problems/boats-to-save-people/
# Submitted: 2026-11-21 15:58 EST
# Intuition: Give the heaviest remaining person a boat and pair them with
# the lightest remaining person whenever the weight limit permits.
# Approach: Sort weights in descending order and move pointers inward,
# counting one boat for each heaviest person processed.
# Complexity: O(n log n) time and O(n) extra space for Python's sort.


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort(key=lambda x: -x)
        total = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                left += 1
            total += 1

        return total
