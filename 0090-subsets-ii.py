# 90. Subsets II
# Problem: https://leetcode.com/problems/subsets-ii/
# Submitted: 2026-08-31 13:53 EDT
# Intuition: Sorting puts duplicates together so skipped runs avoid duplicate subsets.
# Approach: Backtrack with and without each number, skipping its equal run in the exclude branch.
# Complexity: O(n*2^n) time and output space; O(n) auxiliary space.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        answers = []
        nums.sort()

        def explore(i, current):

            if i == len(nums):
                answers.append(current.copy())
                return
            
            # explore with i
            current.append(nums[i])
            explore(i+1, current)

            # explore without i
            current.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            explore(i+1, current)
        
        explore(0, [])

        return answers
                