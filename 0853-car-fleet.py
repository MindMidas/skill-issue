# 853. Car Fleet
# Problem: https://leetcode.com/problems/car-fleet/
# Submitted: 2026-08-23 15:42 EDT
# Intuition: A car joins the fleet ahead if it reaches the destination no later than that fleet.
# Approach: Sort by position, scan backward, and count strictly increasing arrival times.
# Complexity: O(n log n) time, O(n) space.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ps = list(zip(position, speed))
        ps.sort()
        
        total_fleets = 0
        fleet_time = 0

        for i in range(len(ps)-1, -1, -1):
            ttt = (target - ps[i][0]) / ps[i][1]

            if ttt > fleet_time:
                fleet_time = ttt
                total_fleets += 1

        return total_fleets
            
            
        