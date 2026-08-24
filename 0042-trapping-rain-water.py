# 42. Trapping Rain Water
# Problem: https://leetcode.com/problems/trapping-rain-water/
# Submitted: 2026-08-24 12:52 EDT
# Intuition: The shorter boundary determines how much water its side can hold.
# Approach: Move two pointers inward, tracking each side's maximum and accumulating trapped water.
# Complexity: O(n) time, O(1) space.

class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        total_water = 0

        while left < right:

            # left side is shorter or equal to right
            if height[left] <= height[right]:
                # new tallest left otherwise position can hold water
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
            
                left += 1

            # right side is shorter or equal to left
            else:
                # new tallest right otherwise position can hold water
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                
                right -= 1
        
        return total_water