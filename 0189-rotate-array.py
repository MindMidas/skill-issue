# 189. Rotate Array
# Problem: https://leetcode.com/problems/rotate-array/
# Submitted: 2026-10-26 14:22 EDT
# Intuition: Each value belongs at (i + k) % n, and these destinations form cycles.
# Approach: Carry displaced values around each cycle, starting another cycle until all n values have moved.
# Complexity: O(n) time, O(1) extra space.

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        remaining_moves = n
        dummy = nums[0]

        start = 0
        i = start
        
        while remaining_moves:

            # get the dest index
            dest_index = (i + k) % n

            # store value in dest and copy old dest value in dummy
            nums[dest_index], dummy = dummy, nums[dest_index]

            # continue at dest index
            i = dest_index

            # decrement remaining
            remaining_moves -= 1

            # if cycle is complete, start a new one
            if i == start:
                start += 1

                # only start if there's remaining moves
                if remaining_moves:
                    i = start
                    dummy = nums[start]
        
        return nums


# Alternative: Three reversals
# Intuition: Split the array into A + B, where B is the last k elements; rotation wants B + A.
# Approach: Reverse everything to get reversed(B) + reversed(A), then reverse each block to restore its order.
# Complexity: O(n) time, O(1) extra space.

class ReversalSolution:
    def rotate(self, nums: list[int], k: int) -> None:
        if not nums:
            return

        n = len(nums)
        k %= n

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # [1,2,3,4,5,6,7], k = 3
        reverse(0, n - 1)  # [7,6,5,4,3,2,1]
        reverse(0, k - 1)  # [5,6,7,4,3,2,1]
        reverse(k, n - 1)  # [5,6,7,1,2,3,4]
