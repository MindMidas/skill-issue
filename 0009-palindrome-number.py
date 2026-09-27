# 9. Palindrome Number
# Problem: https://leetcode.com/problems/palindrome-number/
# Submitted: 2026-09-27 18:23 EDT
# Intuition: A palindrome has matching digits at mirrored positions.
# Approach: Reject negatives, convert to a string, and compare inward with two pointers.
# Complexity: O(d) time, O(d) space; d is the number of digits.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        left = 0
        x = str(x)
        right = len(x) - 1

        while left <= right:

            if int(x[left]) != int(x[right]):
                return False
            else:
                left += 1
                right -= 1
        
        return True
