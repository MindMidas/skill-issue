# 169. Majority Element
# Problem: https://leetcode.com/problems/majority-element/
# Submitted: 2026-11-08 17:32 EST
# Intuition: The majority element is the value whose frequency exceeds half the array length.
# Approach: Count each value in a dictionary and return as soon as its count exceeds n // 2.
# Complexity: O(n) average time and O(n) space.

class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        # use a freq dict
        n = len(nums)
        freq = {}

        for num in nums:

            # increment freq
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

            # check if majority element
            if freq[num] > (n // 2):
                return num
