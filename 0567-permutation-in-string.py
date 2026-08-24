# 567. Permutation in String
# Problem: https://leetcode.com/problems/permutation-in-string/
# Submitted: 2026-08-24 15:26 EDT
# Intuition: A permutation has exactly the same character counts in a window of equal length.
# Approach: Slide a fixed-length window, maintaining and comparing its frequency dictionary.
# Complexity: O(n + m) time, O(1) space for the lowercase alphabet.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        seen = {}
        need = {}
        left = 0

        # needed frequency
        for char in s1:
            need[char] = need.get(char, 0) + 1


        for right, char in enumerate(s2):
            
            # add char to seen
            seen[char] = seen.get(char, 0) + 1

            # ensure window doesn't get any longer
            while right - left + 1 > len(s1):

                # remove left char from seen
                seen[s2[left]] -= 1

                # remove from dict if 0 
                if seen[s2[left]] == 0:
                    del seen[s2[left]]
                
                left += 1

            # cmp length and dicts
            if right - left + 1 == len(s1) and seen == need:
                return True

        return False
                
            

            
        
   