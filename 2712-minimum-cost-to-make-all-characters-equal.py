# 2712. Minimum Cost to Make All Characters Equal
# Problem: https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/
# Submitted: 2026-11-04 15:00 EST
# Intuition: A prefix or suffix flip only changes whether the two bits at its boundary match.
# Approach: For each pair of different neighbors, add the cost of flipping the shorter side.
# Complexity: O(n) time and O(1) extra space.

class Solution:
    def minimumCost(self, s: str) -> int:

        n = len(s)
        cost = 0

        for i in range(n-1):

            # fix this boundary if the neighbors differ
            if s[i] != s[i+1]:

                # flip the shorter side
                cost += min(i+1, n-i-1)

        return cost
