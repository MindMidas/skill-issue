# 84. Largest Rectangle in Histogram
# Problem: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Submitted: 2026-08-23 16:24 EDT
# Intuition: A bar's rectangle ends when a shorter bar appears to its right.
# Approach: Maintain increasing heights with their earliest starts and evaluate them when popped.
# Complexity: O(n) time, O(n) space.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = list()
        max_area = 0

        for i, curr_height in enumerate(heights):
            start = i

            # if current bar is SHORTER than bar on top of stack, taller bar cannot continue anymore
            while stack and stack[-1][1] > curr_height:

                # remove taller bar
                index, height = stack.pop()

                # calculate width and area
                width = i - index
                area = width * height

                # is it largest
                max_area = max(max_area, area)

                # current shorter bar can extend back to where popped taller bar started
                start = index

            # store current bar + earliest index it can extend to
            stack.append((start, curr_height))
            
        # Any bars still in the stack never found a shorter bar to their right
        # So they can extend all the way to the end
        for index, height in stack:

            width = len(heights) - index
            area = height * width

            max_area = max(max_area, area)

        return max_area