# 2166. Design Bitset
# Problem: https://leetcode.com/problems/design-bitset/
# Submitted: 2026-11-15 12:43 EST
# Intuition: A flip flag lets us invert all bits without visiting each one.
# Approach: XOR each stored bit with the flip flag to get its current value.
# Track the number of ones and replace it with the number of zeros on a flip.
# Complexity: O(n) time for initialization and toString, O(1) time for all
# other operations, and O(n) space for n bits.


class Bitset:
    def __init__(self, size: int):
        self.bitset = [0] * size
        self.total_ones = 0
        self.flipped = False

    def fix(self, idx: int) -> None:
        actual = self.bitset[idx] ^ self.flipped
        if not actual:
            self.bitset[idx] = 1 ^ self.flipped
            self.total_ones += 1

    def unfix(self, idx: int) -> None:
        actual = self.bitset[idx] ^ self.flipped
        if actual:
            self.bitset[idx] = 0 ^ self.flipped
            self.total_ones -= 1

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.total_ones = len(self.bitset) - self.total_ones

    def all(self) -> bool:
        return len(self.bitset) == self.total_ones

    def one(self) -> bool:
        return self.total_ones > 0

    def count(self) -> int:
        return self.total_ones

    def toString(self) -> str:
        return "".join(str(bit ^ self.flipped) for bit in self.bitset)
