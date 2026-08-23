# 15. 3Sum
# Problem: https://leetcode.com/problems/3sum/
# Submitted: 2026-08-23 19:39 EDT
# Intuition: Sorting turns each fixed value's remaining two-sum search into a two-pointer scan.
# Approach: Fix each distinct first value, move inward by the sum, and skip matching duplicates.
# Complexity: O(n^2) time, O(n + k) space including sorting and k output triplets.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        solutions= []
        nums.sort()

        for i in range(len(nums)):
            
            left = i + 1 # avoids duplicate triplets
            right = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                
                total = nums[i] + nums[left] + nums[right]

                # check if we need smaller or larger
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    solutions.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip duplicate values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    
        return solutions
