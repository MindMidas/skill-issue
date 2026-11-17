# 907. Sum of Subarray Minimums
# Problem: https://leetcode.com/problems/sum-of-subarray-minimums/
# Submitted: 2026-11-17 14:29 EST
# Learning note: I found this challenging. My initial intuition was brute force,
# and I used a YouTube tutorial to understand the optimized approach.
# Intuition: Count how many subarrays use each element as their minimum.
# Approach: Maintain a monotonic stack of indices. A smaller value fixes the
# right boundary of each popped element, while its remaining predecessor fixes
# the left boundary. Flush remaining contributions using the end of the array.
# Complexity: O(n) time and O(n) space.


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = (10 ** 9) + 7
        result = 0
        stack = []

        for i, n in enumerate(arr):
            while stack and n < arr[stack[-1]]:
                j = stack.pop()
                right = i - j
                left = j - stack[-1] if stack else j + 1
                result = (result + arr[j] * left * right) % MOD

            stack.append(i)

        for i in range(len(stack)):
            j = stack[i]
            left = j - stack[i - 1] if i > 0 else j + 1
            right = len(arr) - j
            result = (result + arr[j] * left * right) % MOD

        return result
