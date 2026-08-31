# 131. Palindrome Partitioning
# Problem: https://leetcode.com/problems/palindrome-partitioning/
# Submitted: 2026-08-31 16:21 EDT
# Intuition: Each next piece must be a palindrome before exploring the remaining suffix.
# Approach: Try every next substring, compare it with its reverse, and backtrack over valid pieces.
# Complexity: O(n^2*2^n) upper-bound time, O(n*2^n) output space; O(n^2) auxiliary upper bound.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        valid = []

        def explore(i, current):

            if i == len(s):
                valid.append(current.copy())
                return
            
            for j in range(i, len(s)):
                substring = s[i:j+1]

                if substring == substring[::-1]:
                    current.append(substring)
                    explore(j+1, current)
                    current.pop()

        
        explore(0,[])
        return valid