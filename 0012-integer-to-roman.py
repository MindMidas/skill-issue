# 12. Integer to Roman
# Problem: https://leetcode.com/problems/integer-to-roman/
# Submitted: 2026-09-21 14:38 EDT
# Intuition: Taking the largest available Roman value also handles subtractive pairs.
# Approach: Repeatedly subtract values in descending order and append their symbols.
# Complexity: O(1) time and space under the problem's fixed range (1..3999).

class Solution:
    def intToRoman(self, num: int) -> str:
        
        values = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        roman_sol= ""

        for value, roman in values:
            
            while num >= value:
                num -= value
                roman_sol += roman
        
        return roman_sol