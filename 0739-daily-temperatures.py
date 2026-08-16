# 739. Daily Temperatures
# Problem: https://leetcode.com/problems/daily-temperatures/
# Submitted: 2026-08-16 19:50 EDT
# Intuition: A warmer day resolves all cooler days waiting at the top of the stack.
# Approach: Keep unresolved indices in a decreasing-temperature stack and fill waits when popped.
# Complexity: O(n) time, O(n) space.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                
                answer[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)


        return answer