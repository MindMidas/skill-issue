# 735. Asteroid Collision
# Problem: https://leetcode.com/problems/asteroid-collision/
# Submitted: 2026-10-23 13:50 EDT
# Intuition: Keep survivors in result; a left-moving asteroid can hit right-moving ones at the end.
# Approach: Use result as a stack, resolve collisions from its end, and append the asteroid if it survives.
# Complexity: O(n) time, O(n) space; each asteroid is appended and popped at most once.

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        result = []

        for a in asteroids:

            while result and result[-1] > 0 and a < 0:
                if result[-1] < -a:
                    result.pop()
                elif result[-1] == -a:
                    result.pop()
                    break
                else:
                    break
            else:
                result.append(a)

        return result

