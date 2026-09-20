# 412. Fizz Buzz
# Problem: https://leetcode.com/problems/fizz-buzz/
# Submitted: 2026-09-20 16:32 EDT
# Intuition: Divisibility by both 3 and 5 must be checked before either alone.
# Approach: Build the output from 1 to n using divisibility checks.
# Complexity: O(n log n) time and output space counting decimal characters; O(1) auxiliary space.

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        solution = []
        
        for i in range(1, n+1):

            if i % 3 == 0 and i % 5 == 0:
                solution.append("FizzBuzz")
            elif i % 3 == 0:
                solution.append("Fizz")
            elif i % 5 == 0:
                solution.append("Buzz")
            else:
                solution.append(str(i))
        
        return solution