# 18. 4Sum
# Problem: https://leetcode.com/problems/4sum/
# Submitted: 2026-09-15 15:59 EDT
# Intuition: Sorting lets two pointers search the remaining pair after fixing two values.
# Approach: Try each first pair, move inward by the sum, and deduplicate tuples in a set.
# Complexity: O(n^3 + k) time, O(n + k) space including sorting and k unique results.

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        
        result = set()
        nums.sort()

        for i in range(len(nums) - 3):

            for j in range(i + 1, len(nums) - 2):

                left = j + 1
                right = len(nums) - 1

                while left < right:

                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        quplet = (nums[i], nums[j], nums[left], nums[right])
                        result.add(quplet)

                        left += 1
                        right -= 1
        
        return [list(x) for x in result]