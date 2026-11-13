# 2671. Frequency Tracker
# Problem: https://leetcode.com/problems/frequency-tracker/
# Submitted: 2026-11-13 11:40 EST
# Intuition: Grouping numbers by frequency makes it quick to tell whether a frequency is present.
# Approach: Keep each number's count and a set of numbers for each positive count. Move a number between sets when its count changes.
# Complexity: O(1) average time per operation and O(d + f) space for d distinct numbers seen and f frequency buckets created.

class FrequencyTracker:
    def __init__(self):
        self.nums = {}  # Numbers for a given frequency.
        self.freq = {}  # Frequency of a number.

    def add(self, number: int) -> None:
        if number not in self.freq:
            self.freq[number] = 0

        self.freq[number] += 1

        if self.freq[number] not in self.nums:
            self.nums[self.freq[number]] = set()

        self.nums[self.freq[number]].add(number)
        if self.freq[number] > 1:
            self.nums[self.freq[number] - 1].remove(number)

    def deleteOne(self, number: int) -> None:
        if number in self.freq and self.freq[number] > 0:
            self.nums[self.freq[number]].remove(number)
            self.freq[number] -= 1

            if self.freq[number] > 0:
                self.nums[self.freq[number]].add(number)

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.nums and len(self.nums[frequency]) > 0:
            return True

        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
