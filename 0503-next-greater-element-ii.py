# 503. Next Greater Element II
# Problem: https://leetcode.com/problems/next-greater-element-ii/
# Submitted: 2026-11-21 17:20 EST
# Intuition: A decreasing stack holds indices waiting for their next greater value.
# Approach: Traverse the array twice using modular indices to handle circular
# order. Resolve smaller stacked values and push indices only on the first pass.
# Complexity: O(n) time and O(n) space.


class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        stack = []
        result = [-1] * n

        for i in range(2 * n):
            index = i % n
            num = nums[index]
            while stack and num > nums[stack[-1]]:
                j = stack.pop()
                result[j] = num

            if i < n:
                stack.append(index)

        return result
