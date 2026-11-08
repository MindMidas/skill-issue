# 680. Valid Palindrome II
# Problem: https://leetcode.com/problems/valid-palindrome-ii/
# Submitted: 2026-11-08 17:46 EST
# Intuition: At the first mismatch, a valid single deletion must remove either the left or right character.
# Approach: Compare characters with two pointers, then check both remaining substrings without further deletions when a mismatch occurs.
# Complexity: O(n) time and O(1) extra space.

class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        # helper to test left/right removal options
        def isRemainingPalindrome(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # check palindrome till mismatch
        while left <= right:

            # unequal so try removing left and see if it helps else try removing right
            if s[left] != s[right]:
                return isRemainingPalindrome(left+1,right) or isRemainingPalindrome(left, right-1)

            # equal simply increment both ptr inwards
            left += 1
            right -= 1

        return True
