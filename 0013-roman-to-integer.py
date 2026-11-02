# 13. Roman to Integer
# Problem: https://leetcode.com/problems/roman-to-integer/
# Submitted: 2026-11-02 18:41 EST
# Intuition: Read subtractive pairs like IV as one value; otherwise add the current symbol.
# Approach: Use a lookup table for symbols and pairs, checking two characters before consuming one.
# Complexity: O(n) time, O(1) extra space.

class Solution:
    def romanToInt(self, s: str) -> int:
        
        r_to_i = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
        }

        i = 0
        total = 0

        while i < len(s):

            # check two letters first to handle subtractive pairs like IV
            if s[i:i+2] in r_to_i:
                total += r_to_i[s[i:i+2]]
                i += 2
            else:
                # otherwise consume one symbol
                total += r_to_i[s[i]]
                i += 1
        
        return total
