# 2241. Design an ATM Machine
# Problem: https://leetcode.com/problems/design-an-atm-machine/
# Submitted: 2026-11-10 18:27 EST
# Intuition: Track the inventory of each denomination and calculate a withdrawal before deducting any notes.
# Approach: Add deposits by denomination. For a withdrawal, take as many available notes as possible from largest to smallest, then deduct them only if they cover the full amount.
# Complexity: O(1) time per operation and O(1) space for the five fixed denominations.

class ATM:

    def __init__(self):
        self.notes = {
            500: 0,
            200: 0,
            100: 0,
            50: 0,
            20: 0
        }

    def deposit(self, banknotesCount: list[int]) -> None:
        values = {
            4: 500,
            3: 200,
            2: 100,
            1: 50,
            0: 20
        }

        for i in range(4, -1, -1):
            self.notes[values[i]] += banknotesCount[i]

    def withdraw(self, amount: int) -> list[int]:
        notes_count = [0] * 5

        for i, note in enumerate(self.notes):
            take = min(self.notes[note], amount // note)

            notes_count[4-i] = take
            amount -= take * note

        if amount > 0:
            return [-1]
        else:
            for i, note in enumerate(self.notes):
                self.notes[note] -= notes_count[4-i]

        return notes_count


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
