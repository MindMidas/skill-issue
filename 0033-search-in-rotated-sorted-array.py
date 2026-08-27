# 33. Search in Rotated Sorted Array
# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Submitted: 2026-08-26 20:30 EDT
# Intuition: At least one half around the midpoint is sorted despite the rotation.
# Approach: Identify the sorted half and keep it only if its range contains the target.
# Complexity: O(log n) time, O(1) space.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0 
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1