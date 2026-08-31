# 46. Permutations
# Problem: https://leetcode.com/problems/permutations/
# Submitted: 2026-08-31 13:46 EDT
# Intuition: Each position can hold any of the unused values.
# Approach: Swap each candidate into the current position, recurse, and undo the swap.
# Complexity: O(n*n!) time and output space; O(n) auxiliary recursion space.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        answer = []

        def explore(i):

            if i == len(nums):
                answer.append(nums.copy())
                return 

            for j in range(i, len(nums)):
                swap(i,j)
                explore(i+1)
                swap(i,j)
    
        explore(0)
        return answer
