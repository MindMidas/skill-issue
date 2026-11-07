# 905. Sort Array By Parity
# Problem: https://leetcode.com/problems/sort-array-by-parity/
# Submitted: 2026-11-07 13:30 EST
# Intuition: The prefix before swap_odd contains only even numbers.
# Approach: Scan the array and swap each even number into the next position in the even prefix.
# Complexity: O(n) time and O(1) extra space.

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:

        swap_odd = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[swap_odd] = nums[swap_odd], nums[i]
                swap_odd+=1

        return nums
