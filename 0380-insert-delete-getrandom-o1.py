# 380. Insert Delete GetRandom O(1)
# Problem: https://leetcode.com/problems/insert-delete-getrandom-o1/
# Submitted: 2026-11-07 18:15 EST
# Intuition: An array supports random access, while a value-to-index map makes each value easy to locate.
# Approach: Append on insertion; remove by moving the last element into the removed value's slot and updating its index. Choose a random array element for getRandom.
# Complexity: O(1) average amortized time for insert and remove, O(1) time for getRandom, and O(n) space.

import random
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.index = {}

    def insert(self, val: int) -> bool:

        # insert is simple, so just append and log new index
        if val not in self.index:
            self.nums.append(val)
            self.index[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:

        if val in self.index:

            # move last inserted to index of val being removed
            self.index[self.nums[-1]] = self.index[val]
            self.nums[self.index[val]] = self.nums[-1]

            # pop end from nums
            self.nums.pop()
            del self.index[val]

            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
