# 16. 3Sum Closest
# Problem: https://leetcode.com/problems/3sum-closest/
# Submitted: 2026-09-15 15:48 EDT
# Intuition: After sorting, moving either end changes the triplet sum predictably.
# Approach: Fix one value, scan with two pointers, and retain the closest sum.
# Complexity: O(n^2) time, O(n) worst-case space for Python sorting.

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                curr_total =  nums[i] + nums[left] + nums[right]

                if abs(curr_total - target) < abs(closest - target):
                    closest = curr_total
                
                if curr_total < target:
                    left += 1
                elif curr_total > target:
                    right -= 1
                else:
                    return target


        return closest