# 40. Combination Sum II
# Problem: https://leetcode.com/problems/combination-sum-ii/
# Submitted: 2026-08-31 13:23 EDT
# Intuition: Sorting lets the exclude branch skip equal values and avoid duplicate combinations.
# Approach: Backtrack by taking each candidate once or skipping its duplicate run.
# Complexity: O(n*2^n) worst-case time and output space; O(n) auxiliary space.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        answers = []
        candidates.sort()

        def explore(i, current):

            total = sum(current)

            if total == target:
                answers.append(current.copy())
                return

            if total > target:
                return
                
            if i >= len(candidates):
                return
            
            current.append(candidates[i])
            explore(i+1, current)

            current.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
                
            explore(i+1, current)

        explore(0, [])
        return answers