# 39. Combination Sum
# Problem: https://leetcode.com/problems/combination-sum/
# Submitted: 2026-08-31 13:03 EDT
# Intuition: A candidate can be reused, but once skipped it never needs revisiting.
# Approach: Backtrack by taking the current value again or moving to the next candidate.
# Complexity: O(R*(D+1)) time, O(n + D + out) space; R calls, D=target/min(candidates), out output size.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        answers = []

        def explore(i, current):

            total = sum(current)
            
            if total > target:
                return
            
            if total == target:
                answers.append(current.copy())
                return

            if i >= len(candidates):
                return
            
            current.append(candidates[i])
            explore(i, current)

            current.pop()
            explore(i+1, current)

        explore(0, [])
        return answers
                