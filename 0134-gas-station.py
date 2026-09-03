# 134. Gas Station
# Problem: https://leetcode.com/problems/gas-station/
# Submitted: 2026-09-03 11:49 EDT
# Intuition: If a route's balance becomes negative, none of its visited starts can work.
# Approach: Track total and current surplus, resetting the candidate start after a deficit.
# Complexity: O(n) time, O(1) space.

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        curr_sum = 0
        start_index = 0
        total_sum = 0

        for i, station in enumerate(gas):
            
            total_sum += station - cost[i]
            curr_sum += station - cost[i]

            if curr_sum < 0:
                curr_sum = 0
                start_index = i+1
        
        if total_sum < 0:
            return -1
        
        return start_index
