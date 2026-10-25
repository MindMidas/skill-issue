# 1014. Best Sightseeing Pair
# Problem: https://leetcode.com/problems/best-sightseeing-pair/
# Submitted: 2026-10-25 15:32 EDT
# Intuition: Split the score into (values[i] + i) + (values[j] - j), keeping the best earlier left term.
# Approach: Scan j left to right, update the score with best_left, then consider j as a future left endpoint.
# Complexity: O(n) time, O(1) extra space.

class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        
        # keep track of best left value and score
        best_left = values[0]
        best_score = float("-inf")

        # scan left to right updating best score and using best left
        for j in range(1, len(values)):

            # update best score and best left
            best_score = max(best_score, best_left + values[j] - j) 
            best_left = max(best_left, values[j]+j)
        
        return best_score