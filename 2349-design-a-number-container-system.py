# 2349. Design a Number Container System
# Problem: https://leetcode.com/problems/design-a-number-container-system/
# Submitted: 2026-11-12 11:41 EST
# Intuition: A min heap can find the smallest index for a number, while a dictionary tells whether that index still holds the number.
# Approach: Push each assignment onto its number's heap and update the index map. When finding a number, discard stale heap entries until the top index is valid.
# Complexity: O(log q) per change and O(1 + k log q) per find that removes k stale entries. Space is O(q) for q changes.

import heapq


class NumberContainers:
    def __init__(self):
        self.nums = {}
        self.min_index = {}

    def change(self, index: int, number: int) -> None:
        # Push the index to the heap for this number.
        if number not in self.min_index:
            self.min_index[number] = []
        heapq.heappush(self.min_index[number], index)

        # Store the current number at this index.
        self.nums[index] = number

    def find(self, number: int) -> int:
        if number not in self.min_index:
            return -1

        # Discard indexes that have been assigned a different number.
        while self.min_index[number] and number != self.nums[self.min_index[number][0]]:
            heapq.heappop(self.min_index[number])

        if self.min_index[number]:
            return self.min_index[number][0]

        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
