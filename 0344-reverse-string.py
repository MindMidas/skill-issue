# 344. Reverse String
# Problem: https://leetcode.com/problems/reverse-string/
# Submitted: 2026-11-04 12:33 EST
# Intuition: Swapping mirrored characters reverses the string in place.
# Approach: Walk to the midpoint and swap each character with its counterpart from the end.
# Complexity: O(n) time and O(1) space.

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        # swaps till midpoint
        for i in range(n//2):

            # get target
            target = n - i - 1

            # swap
            s[i], s[target] = s[target], s[i]
