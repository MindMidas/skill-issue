# 31. Next Permutation
# Problem: https://leetcode.com/problems/next-permutation/
# Submitted: 2026-11-09 14:07 EST
# Intuition: Increase the rightmost possible position, then make its suffix as small as possible.
# Approach: Find the rightmost ascending pair, swap the pivot with the rightmost greater value, and reverse the descending suffix. Reverse the whole array if no pivot exists.
# Complexity: O(n) time and O(1) extra space.

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # intuition: find rightmost position we can increase the num,
        # then swap and arrange everything after in ascending order

        n = len(nums)

        for i in range(n-2, -1, -1):

            # greater adjacent rule
            if nums[i] < nums[i+1]:

                # find smallest number greater than nums[i] to its right
                # we know numbers to the right are in descending order
                for j in range(n-1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break

                left, right = i+1, n-1

                # we know its descending so we just need to swap
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    right-=1
                    left+=1

                return

        # at this point we know nums is in reverse, so reverse and return
        nums.reverse()
        return
