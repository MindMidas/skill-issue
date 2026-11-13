# 2502. Design Memory Allocator
# Problem: https://leetcode.com/problems/design-memory-allocator/
# Submitted: 2026-11-13 11:13 EST
# Intuition: The first run of enough zeroes is the leftmost available block.
# Approach: Scan for consecutive free cells and mark the first block that fits. Free memory by clearing every cell with the requested ID.
# Complexity: O(n) time per operation and O(n) space for n memory cells.

class Allocator:
    def __init__(self, n: int):
        self.memory = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        start = -1
        count = 0

        for i in range(len(self.memory)):
            if self.memory[i] == 0:
                count += 1
            else:
                count = 0

            if count == size:
                start = i - size + 1

                for j in range(start, start + size):
                    self.memory[j] = mID

                return start

        return start

    def freeMemory(self, mID: int) -> int:
        freed = 0
        for i in range(len(self.memory)):
            if self.memory[i] == mID:
                self.memory[i] = 0
                freed += 1

        return freed


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
