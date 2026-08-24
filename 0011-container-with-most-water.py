# 11. Container With Most Water
# Problem: https://leetcode.com/problems/container-with-most-water/
# Submitted: 2026-08-23 20:41 EDT
# Intuition: Moving the taller boundary cannot improve a container limited by the shorter one.
# Approach: Measure each two-pointer container and move its shorter boundary inward.
# Complexity: O(n) time, O(1) space.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:

            max_area = max(((right-left)*min(height[left], height[right])), max_area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_area


        
