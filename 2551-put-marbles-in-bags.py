# 2551. Put Marbles in Bags
# Problem: https://leetcode.com/problems/put-marbles-in-bags/
# Submitted: 2026-11-02 19:05 EST
# Intuition: Each cut adds the two adjacent weights; the outer endpoints are fixed and cancel in the difference.
# Approach: Sort all adjacent pair sums and subtract the sum of the k - 1 smallest from the k - 1 largest.
# Complexity: O(n log n) time, O(n) extra space; O(1) time and space when k = 1.

class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        
        # no score diff, one bag
        if k == 1:
            return 0

        # store the score contribution of every possible cut
        cuts = []

        # n-1 possible cuts between adjacent marbles
        # each cut adds the last marble of one bag and first of the next
        for i in range(len(weights) - 1):
            cuts.append(weights[i] + weights[i+1])
        
        # sort cuts
        cuts.sort()
        
        # sum k-1 smallest cuts
        min_score = sum(cuts[:k-1])

        # sum k-1 largest cuts
        max_score = sum(cuts[-(k-1):])

        # first and last weights are shared by every partition, so they cancel
        return max_score - min_score
