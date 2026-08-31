# 78. Subsets
# Problem: https://leetcode.com/problems/subsets/
# Submitted: 2026-08-31 12:53 EDT
# Intuition: Every element has two independent choices: include it or exclude it.
# Approach: Backtrack over both choices and copy the current subset at each leaf.
# Complexity: O(n*2^n) time and output space; O(n) auxiliary space.

class Solution: 

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        answer = []

        def explore(i, current):

            if i == len(nums):
                answer.append(current.copy())
                return
            
            # include nums[i]
            current.append(nums[i])
            explore(i+1, current)

            # exclude nums[i]
            current.pop()
            explore(i+1, current)

        
        explore(0, [])

        return answer