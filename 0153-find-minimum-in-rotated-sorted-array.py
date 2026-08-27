# 153. Find Minimum in Rotated Sorted Array
# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Submitted: 2026-08-26 20:00 EDT
# Intuition: Comparing the middle with the right endpoint identifies the side of the rotation.
# Approach: Binary-search while recording the smallest midpoint value seen.
# Complexity: O(log n) time, O(1) space.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        answer = None
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1
            

            if answer is None or nums[mid] <= answer:
                answer = nums[mid]
        
        return answer