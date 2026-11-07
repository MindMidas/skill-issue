# 456. 132 Pattern
# Problem: https://leetcode.com/problems/132-pattern/
# Submitted: 2026-11-07 11:52 EST
# Intuition: A prefix minimum supplies the 1, while a stack of values to the right supplies possible 2s.
# Approach: Scan right to left, discard values no larger than the prefix minimum, and check whether the remaining top fits below nums[j].
# Complexity: O(n) time and O(n) space.

class Solution:
    def find132pattern(self, nums: list[int]) -> bool:

        # i < j < k
        # nums[i] < nums[k] < nums[j]

        # build a prefix-minimum array
        prefix_min = [nums[0]]
        for i in range(1, len(nums)):
            prefix_min.append(min(prefix_min[-1], nums[i]))

        stack = []

        for j in range(len(nums)-1, -1, -1):

            # remove potential k values that are too small
            while stack and stack[-1] <= prefix_min[j]:
                stack.pop()

            # check whether a valid k exists
            if stack and stack[-1] < nums[j]:
                return True

            # add a potential k to the stack
            stack.append(nums[j])


        return False
